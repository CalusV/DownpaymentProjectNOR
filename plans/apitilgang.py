from .models import Laan
import requests

## apitilgang.py brukes i hovedsak av views.py for å forberede data til de forksjellige sidene

##Her bruker vi dataen vi har lagret fra brukerskjemaet til å bygge en payload til APIet
def bygg_payload(laan):
    payload = {
        'laanebelop': laan.laanebelop,
        'nominellRente': laan.nominellRente,
        'terminGebyr': laan.terminGebyr,
        'utlopsDato': laan.utlopsDato.isoformat(),
        'saldoDato': laan.saldoDato.isoformat(),
        'datoForsteInnbetaling': laan.datoForsteInnbetaling.isoformat(),
        'ukjentVerdi': 'TERMINBELOP'
    }
    return payload

##Her kobler vi til APIet og konverter svarer til JSON
def hent_respons(payload):
    API = 'https://visningsrom.stacc.com/dd_server_laaneberegning/rest/laaneberegning/v1/nedbetalingsplan'
    respons = requests.post(API, json=payload)
    json_respons = respons.json()
    return json_respons

