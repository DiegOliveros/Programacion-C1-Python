# -*- coding: utf-8 -*-
"""
# ******** SEMANA 5 ***********
Created on Sat May 17 10:48:19 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [importando archivos csv]
# =============================================================================
# ¿Cuántos son los atletas que tienen el pulso entre 100 y 120?
# =============================================================================
"""

import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/DiegOliveros/Programacion-C1-Python/main/C%C3%B3digo%20Clase/S4%202022%2005%2010/atleta2.csv", sep=",") # separadores "|" "," ";" ":" 
                                                 # "t"o "\t" =no es el simbolo t sino que es un tabulador "tab" 
print(df.to_string()) #todo el archivo 
#print(df.head(5))   #los 5 primeros 
# print(df.tail(5))   #los 5 ultimos 
# print(df.describe())   #los 5 primeros 

df2=df.loc[0:2]
print(df2)

df2=df.loc[2:5]
print(df2)

df2=df.loc[[1,2,3]]
print(df2)

df2=df.loc[3:3]
print(df2)


print((df.loc[0])[2]) 
a=(df.loc[0])
# print(type(df.loc[2]))
cont=1
for i in df.loc[2]:
    cont+=1
    if cont==3:
        print(i)
        
#cuántos atletas tienen el pulso entre 100 y 120 
cont=0
# serie =(df.loc[0:168])[3]
serie2=df.filter(["Pulse"])
serie3=[101,102,103, 120,5,4,3,2]

#declarando funciones

def sano(serie):
    cont=0
    for i in serie:
        #print(i)
        if 136<=i and i<=150:   #if 1>=100 and 120>=i:
            cont+=1
    return cont

def sano2(serie, rango):
    cont=0
    for i in serie:
        #print(i)
        if rango[0]<=i and i<=rango[1]:   #if 1>=100 and 120>=i:
            cont+=1
    return cont    
   
print("los atletas que tienen el pulso entre 100 y 120 son: ", sano(serie3))

serie4=df.iloc[:,2]
print("los atletas que tienen el pulso entre 100 y 120 son: ",sano(serie4))

print("Usando la función sano 2:")

rango=[100,150]
print("los atletas que tienen el pulso entre",rango[0]," y "
      ,rango[1]," son: ",sano2(serie4,rango))

rango=[136,150]
print("los atletas que tienen el pulso entre",rango[0]," y "
      ,rango[1]," son: ",sano2(serie4,rango))


rango=[50,80]
print("los atletas que tienen el pulso entre",rango[0]," y "
      ,rango[1]," son: ",sano2(serie4,rango))




