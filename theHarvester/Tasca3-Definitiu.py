#!/bin/python
# Importem les llibreries de Shodan, requests i sys
import requests
import sys
from shodan import Shodan

# Import per cridar l'eina theHarvester
import asyncio
import aiodns
import subprocess


# Demana a l'usuari una ip que la guardara en la variable dades.
dades = input("Disme la ip que vols buscar: ")
# Setup de API de (Sergi)
api = Shodan('iyw7Is1pCQ2kCoqAn6KNEQvpT2VlqBpo')

# Crearem dos variables una que guardarem la informació del equip que està a l'API de Shodan.
result = api.host(dades)
results = api.search(dades)

try:
    # Bucle que recorre la informació de l'API:
    for service in result['data']:
        # Mostra el domini, la ip i els ports oberts trobats l'API;
        print(service['domains'], service['ip_str'], service['port'])
        domain=service['domains']

    try:
        # Demana un nom de servei a l'usuari:
        dades2 = input("Introdueix un servei: ")
        # Buscara en l'API els resultats del servei indicat per l'usuari
        results = api.search(dades2)
        # Mostra els resultats obtinguts del servei i la IP indicats anteriorment
        print('Resultats obtinguts: {}' . format(results['total']))
        for result2 in results['matches']:
            print('IP: {}' . format(service['ip_str']))
            print(result2['data'])
            print('')
    except Shodan.APIError:
        print('Error: {}' . format(Shodan.APIError))
except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)



subprocess.call("python3 ./theHarvester.py -d {} -l 10 -b google".format(domain), shell=True)





