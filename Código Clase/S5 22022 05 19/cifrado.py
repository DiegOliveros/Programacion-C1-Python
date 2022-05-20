# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 **********
Created on Thu May 19 18:54:10 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

def cuadradoycubo(numero):
    return numero**2, numero**3

cuadrado =cuadradoycubo(8)[0]
cubo =cuadradoycubo(8)[1]

cuadrado2, cubo2=cuadradoycubo(3)

print(cuadrado)
print(cubo)


print("3*3=",cuadrado2)
print("3*3*3=",cubo2)