# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Sat May 28 08:20:58 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [fecha.py]   [manipulando archivos csv]
# =============================================================================
# https://github.com/DiegOliveros/MISION-TIC-2020/blob/main/Retos/Taller%202.pdf
# =============================================================================
"""

import datetime as dt
import pytz
import matplotlib.pyplot as plt
import numpy as np 
#algunas aclaraciones sobre el modulo datetime:
fecha = dt.datetime.now()

#posibles formatos
print(fecha, type(fecha))
print(fecha.year)
print(fecha.strftime("%c"))
print(fecha.strftime("%X"))
print(fecha.strftime("%x"))
#otros formatos https://strftime.org/

print('Todas las posibles zonas horarias:')
for timeZone in pytz.all_timezones:
    print(timeZone)   #todas las posibles zonas horarias

#Realizando un cambio de zona horaria  
timezone = pytz.timezone("America/Lima")   #America/Lima en nuestro caso en lugar de Europe/Dublin"
fecha = dt.datetime.now(timezone)
#Imprimiendo el cambio de zona horaria 
print(fecha, type(fecha))
print(fecha.year)

# Desarrollo del ejercicio 
# la descripcción la encuentro en la siguiente url:
#https://github.com/DiegOliveros/MISION-TIC-2020/blob/main/Retos/Taller%202.pdf

i=10
diccionario={}
datos_en_x=[]
datos_en_y=[]
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
         datos_en_x.append(float(altura))
         latitud=input("ingrese la latitud: ")
         datos_en_y.append(float(latitud))
         longitud=input("ingrese la longitud: ")
         diccionario[fecha]=[altura,latitud,longitud]

#formar cadena y guardar
print("la sesión ha terminado")    
for x in diccionario.keys():
    print(x)    
    print(diccionario[x])
    
    file = open("registrotopográfico.csv","a")  #agregar y si no existe, crea y agrega 
    file.write(str(x)+","+str(diccionario[x][0])+","+str(diccionario[x][1])+","+str(diccionario[x][2]))
    file.close()

#hacemos lectura del archivo

file = open("registrotopográfico.csv","r")   #leer
print(file.read())  #texto compleo 
file.close()  

print(datos_en_x)
X,Y=np.meshgrid(datos_en_x,datos_en_y)
Z= 1/(1+np.exp(-X-Y))   # acá se genera la matriz para de valores para la altura
# print(Z, type(Z))
# print(X, type(X))
# print(Y, type(Y))
fig=plt.Figure(figsize=(8,6))
ejes3d=plt.axes(projection="3d")
ejes3d.plot_surface(X,Y,Z,cmap="plasma")


plt.show()


