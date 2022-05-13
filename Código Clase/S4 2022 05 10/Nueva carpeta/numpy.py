# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 12 09:43:13 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [numpy]
# =============================================================================
# 
# =============================================================================
"""

import numpy as np 

rango = np.arange(10,50)  
print(rango)

rango=rango[::-1]   #Invertir el arreglo
print(rango)

a= np.arange(0,6).reshape(3,2)   # i, j filas, columnas 
print(a)

a=np.arange(0,9).reshape(3,3)

print(a)

np.savez("my_array",a,rango, rango,rango)