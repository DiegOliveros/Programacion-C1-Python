# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Thu May 26 18:16:20 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [Trabajando con lista de correo]
# =============================================================================
# 
# =============================================================================
"""

diccionario={'hotmail.com':["leafarsoft", "andres", "juan"]}   #calve, valor
diccionario={'hotmail.com':["leafarsoft", "andres", "juan"],
             "gmail.com":["Andrés", "Rafael", "Jorge", "Sebastian", "Yeison", "luisa"],
             "udea.edu.co":["Andrés", "Rafael", "Jorge", "Sebastian", "Yeison", "luisa"]}   #calve, valor


#Paso 1: 
# def email_list(diccionario):
#     correos = []
#     for usuarios in diccionario.keys():
#         print(usuarios)     # cada uno de los dominios 
#         print(diccionario[usuarios])  #cada una de las listas de cada dominio
        
# email_list(diccionario)


#Paso 2:
def email_list(diccionario):
    correos = []
    for usuarios in diccionario.keys():
        for nombre in diccionario[usuarios]:  # iteración  1 =diccionario[hotmail.com] 
            correos.append(nombre+"@"+usuarios)
    return correos

print(email_list(diccionario))

