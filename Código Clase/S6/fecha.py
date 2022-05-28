# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Sat May 28 08:20:58 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import datetime as dt
import pytz
import pandas as pd

fecha = dt.datetime.now()

print(fecha, type(fecha))
print(fecha.year)
print(fecha.strftime("%c"))
print(fecha.strftime("%X"))
print(fecha.strftime("%x"))


print('Todas las posibles zonas horarias:')
for timeZone in pytz.all_timezones:
    print(timeZone)
    
timezone = pytz.timezone("America/Lima")   #America/Lima en nuestro caso en lugar de Europe/Dublin"
fecha = dt.datetime.now(timezone)

print(fecha, type(fecha))
print(fecha.year)

i=10
diccionario={}
while i !=0:
    i=int(input("""
          Menu
          Ingrese cualquiera de las siquientes opciones:
          1. Igresar registro
          0. Terminar
          """))
    if i==1:
         fecha = dt.datetime.now(timezone)
         altura=input("ingrese la altura: ")
         latitud=input("ingrese la latitud: ")
         longitud=input("ingrese la longitud: ")
         diccionario[fecha]=[altura,latitud,longitud]

    
print("la sesión ha terminado")    
for x in diccionario.keys():
    print(x)    
    print(diccionario[x])
    file = open("registrotopográfico.csv","a")  #agregar y si no existe, crea y agrega 
    file.write(str(x)+","+str(diccionario[x][0])+","+str(diccionario[x][1])+","+str(diccionario[x][2]))
    file.close()



file = open("registrotopográfico.csv","r")   #leer
print(file.read())  #texto compleo 
file.close()  




