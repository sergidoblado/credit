#!/bin/python

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introdueix un numero de l'1 al 4: "))
            correcto=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("Opció 1. API de Shodan")
    print ("Opció 2. theHarvester")
    print ("Opció 3. Bot telegram")
    print ("4. Sortir")
     
    print ("Escull una opció")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opció 1")
        exec(open("APISHODAN.py").read())
    elif opcion == 2:
        print ("Opció 2")
        exec(open("apitheharvester.py").read())
    elif opcion == 3:
        print("Opció 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fi")