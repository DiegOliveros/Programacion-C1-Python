# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 24 19:07:14 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import json

mi_str_json = '{"nombre":"Adriana Lucia","edad":"15","ciudad":"Medellín"}'
mi_str_json2 = {
                "nombre":"Adriana Lucia",
                "edad":"15",
                "ciudad":"Medellín"
                }


mi_json= json.loads(mi_str_json)
print(mi_json)
print("El nombre es: ",mi_json["nombre"])

#en el segundo caso accedemos al diccionario directamente.
print(mi_str_json2["nombre"])














