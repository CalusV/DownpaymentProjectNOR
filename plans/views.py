from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Laaneskjema
from . import apitilgang, DAO

# Index-siden er forsiden vår. Her vil vi presenter Låneskjemaet vi genererer API-payload fra
def index(request):
    if request.method == 'POST':
        form = Laaneskjema(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('oversikt/')
    else:
        form = Laaneskjema()
    return render(request, 'plans/index.html', {'form': form})

# Oversikt-siden er resultatsiden vår. Her presenterer vi oversikt over innbetalinger etter å ha generert databasedata.
def oversikt(request):
    latest_laan = DAO.hent_siste_laan()

    if DAO.finn_relaterte_innbetalinger(latest_laan) == True:
        innbetalinger = DAO.hent_relaterte_innbetalinger(latest_laan)
        context = {
            'laan': latest_laan,
            'innbetalinger': innbetalinger
        }
        return render(request, 'plans/oversikt.html', context)
    else:
        params = apitilgang.bygg_payload(latest_laan)
        nedbetalingsplan = apitilgang.hent_respons(params)
        innbetalingsliste = nedbetalingsplan['nedbetalingsplan']['innbetalinger']
        for innbetaling in innbetalingsliste:
            DAO.legg_til_innbetaling(latest_laan, innbetaling)
        innbetalinger = DAO.hent_relaterte_innbetalinger(latest_laan)

        context = {
            'laan' : latest_laan,
            'innbetalinger' : innbetalinger
        }
        return render(request, 'plans/oversikt.html', context)