# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 24 19:42:36 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
import json 

boleano = True
print("esto es un tipo de dato en python: ",boleano)
print("esto es un tipo de dato en formato json: ",json.dumps(boleano))

boleano = False
print("esto es un tipo de dato en python: ",boleano)
print("esto es un tipo de dato en formato json: ",json.dumps(boleano))


nulo = None
print("esto es un tipo de dato en python: ",nulo)
print("esto es un tipo de dato en formato json: ",json.dumps(nulo))


dicccionario = {
                "nombre":"Adriana Lucia",
                "edad":"15",
                "ciudad":"Medellín"
                }
print("esto es un tipo de dato en python: ",type(dicccionario))
print("esto es un tipo de dato en formato json: ",json.dumps(dicccionario))