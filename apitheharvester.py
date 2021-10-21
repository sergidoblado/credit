#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import aiodns
import subprocess

domain= input("Disme el domini que vols buscar: ")
subprocess.call("cd theHarvester && python3 ./theHarvester.py -d {} -l 10 -b google".format(domain), shell=True)

