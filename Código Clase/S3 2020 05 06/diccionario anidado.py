# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May  5 19:05:47 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [diccionarios anidados]
# =============================================================================
# 
# =============================================================================
"""

diccionario2 = {
    "1":[15,"Rafael","Medellín"],
    "2":[28,"Juan", "password"],
    "3":[10,"Ana"],
    "Pablo":10}
diccionario2[ "Pablo"] =[10, "Bogotá"]

print(diccionario2)

diccionario1 = {
    1:[15,"Rafael","Medellín"],
    2:[28,"Juan", "password"],
    3:[10,"Ana"],
    4:10}
diccionario1[ "Pablo"] =[10, "Bogotá"]

print(diccionario1)

familia ={
    "padre": {
                "nombre":"Juan",
                "año":1950
             }, 
    "madre": {
                "nombre333":"Ana",
                "año":1955
             },
    "hijo 1": {
                "nombre":"Juan primero",
                "año":1990
             },
    "hijo 2": {
                "nombre":"sofia",
                "año":1999
             },
    "hijo 3":{
                "nombre":"Junior",
                "año":2020
             },
    
    
    }
                 
# familia2={'padre': {'nombre': 'Juan', 'año': 1950}, 'madre': {'nombre': 'Ana', 'año': 1955}, 'hijo 1': {'nombre': 'Juan primero', 'año': 1990}, 'hijo 2': {'nombre': 'sofia', 'año': 1999}, 'hijo 3': {'nombre': 'Junior', 'año': 2020}}               
                 
# print(familia)
# print(familia2)
print(familia[ "hijo 2"].get("año"))
familia[ "hijo 2"].update({"año":2021})   #"nombre":"sofia",
print(familia[ "hijo 2"].get("año"))
print(familia)
print(familia["hijo 2"]["año"])

