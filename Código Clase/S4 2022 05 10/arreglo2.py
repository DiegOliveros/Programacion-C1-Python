# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 12 19:14:37 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import numpy as np

arreglo = np.array([1,2,3,4,5,6])
arreglo2 = np.array((1,2,3,4,5,6))

print(arreglo)
print(type(arreglo))
print(type(arreglo[0]))
print(np.__version__)


print(arreglo2)
print(type(arreglo2))
print(type(arreglo2[0]+arreglo[0]))
print(arreglo2[0]+arreglo[0])

print(arreglo[1:3])
print(arreglo[2:])
print(arreglo[:5])


arreglo3=np.array(["manzana","pera", "manzana"])
print(type(arreglo3))

arreglo4 =np.arange(10,50)
print(arreglo4)
print(arreglo4[::-1])

print(arreglo4[5::-1])
print(arreglo4[0:6:1])
print(arreglo4[40:34:-1])

cifrado=np.zeros((0,12))
print(cifrado)
cifrado[7]=0
print(cifrado)





