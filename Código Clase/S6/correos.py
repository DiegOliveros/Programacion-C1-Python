# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Thu May 26 18:16:20 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [coreos.py]   [Trabajando con listas de correo]
# =============================================================================
# Cree una función email_list que reciba un diccionario, que contenga
 nombres de dominio como claves y una lista de usuarios como valores.
 Desarrolle el código para generar una lista que contenga direcciones
 de correo electrónico completas (por ejemplo, diana.prince@gmail.com).
 Obtenga los datos de un json y retorne un xlsx (csv) con una nueva tabla. 
# =============================================================================
"""

diccionario={'hotmail.com':["leafarsoft", "andres", "juan"]}   #clave, valor
diccionario={'hotmail.com':["leafarsoft", "andres", "juan"],
             "gmail.com":["Andrés", "Rafael", "Jorge", "Sebastian", "Yeison", "luisa"],
             "udea.edu.co":["Andrés", "Rafael", "Jorge", "Sebastian", "Yeison", "luisa"]}   #clave, valor


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

