from .models import Laan, Innbetaling
import math

## DAO.py brukes til å kommunisere med databasen. Ved å ha all databasekommunikasjon på ett sted får vi
## løs kopling mot eventuelle endringer i databasestrukturen.

#Se etter lån i databasen
def finn_laan():
    if Laan.objects.last():
        return True
    else:
        return False

#Hent siste lån fra Lånedatabasen
def hent_siste_laan():
    return Laan.objects.last()

#Se etter relaterte innbetalinger
def finn_relaterte_innbetalinger(relatert_laan):
    if Innbetaling.objects.filter(laan=relatert_laan):
        return True
    else:
        return False

#Hent relaterte innbetalinger
def hent_relaterte_innbetalinger(relatert_laan):
    return Innbetaling.objects.filter(laan=relatert_laan)

#Genererer en rekke med innbetalingsobjekter i databasen avhengig av resultat fra nedbetalingsAPI
def legg_til_innbetaling(laan, innbetaling):
    betalingsobjekt = Innbetaling()
    betalingsobjekt.laan = laan
    betalingsobjekt.restgjeld = math.ceil(innbetaling['restgjeld'])
    betalingsobjekt.dato = innbetaling['dato']
    betalingsobjekt.gjeldsbetaling = math.ceil(innbetaling['innbetaling'])
    betalingsobjekt.gebyr = math.ceil(innbetaling['gebyr'])
    betalingsobjekt.renter = math.ceil(innbetaling['renter'])
    betalingsobjekt.total = math.ceil(innbetaling['total'])
    betalingsobjekt.save()