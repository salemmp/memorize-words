import os
import sys
import time
lista = {"hello":"hola",
         "word":"palabra",
         "phone":"celular",
         "hand":"mano",
         "how":"como",
         "people":"gente",
         "leave":"salir",
         "key":"tecla",
         "understand":"entender",
         "can":"poder",
         "we":"nosotros",
         "he":"el",
         "she":"ella",
         "low":"bajo",
         "high":"alto",
         "someone":"alguien",
         "head":"cabeza",
         "table":"mesa",
         "room":"cuarto",
         "bathroom":"baño"}
#contador
aciertos = 0
#obtenemos llaves
llaves = lista.keys()
#################################################
for x in llaves:
    valor = lista.get(x)
    respuesta = input (x +" is? ")
    if respuesta == valor:
        print("correcto!!!")
        aciertos = aciertos + 1
        time.sleep(1)
        
        os.system("cls")
    else:
        print("incorrecto")
        time.sleep(0.3)
        os.system("cls")
##################################################################
if (aciertos >= 1) and (aciertos <5):
    print(str(aciertos)+ '/20')
    salida = input("Mal , sigue estudiando")

if (aciertos >=5) and (aciertos<10):
    print(str(aciertos)+ '/20')
    salida = input("puedes mejorar")

if aciertos >=10 and aciertos <15:
    print(str(aciertos)+ '/20')
    salida = input("intermedio.. nada mal")

if aciertos >=15 and aciertos <20:
    print(str(aciertos)+ '/20')
    salida = input("muy bien ! sigue asi")

if aciertos == 20:
    print(str(aciertos)+ '/20')
    salida = input("Excelente!! ")