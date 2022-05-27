# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Tue May 24 19:25:42 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [typos.py]   []
# =============================================================================
# 
# =============================================================================
"""
import json 

with open("productos.json") as unjson:
    datos=json.load(unjson)
print(type(datos), datos) 

#     print(unjson.read(), type(unjson.read()), type(unjson))

    
# print(json.dumps(unjson.read()))