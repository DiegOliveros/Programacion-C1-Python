# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May  5 16:44:25 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [vestuario.py]
# =============================================================================
# In Python, a dictionary can only hold a single value for a given key. 
To workaround this, our single value can be a list containing multiple values.
 Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
 Fill in the blanks to print a line for each item of clothing with each color, 
 for example: "red shirt", "blue shirt", and so on.

# =============================================================================
"""

vestuario={
    "shirt":["rojo", "azul", "white"],
    "jeans":[]
    }

print(vestuario)

lista=input("ingrese los colores de los pantalones")

vestuario.update({"jeans":[lista[0:4],lista[4:9]]})
print(vestuario)

# for llave in vestuario:
#     print(llave)

for llavevestuario in vestuario.keys():
    for items in vestuario[llavevestuario]:
        print(items, "**", llavevestuario)







