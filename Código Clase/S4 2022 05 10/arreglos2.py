# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 14 08:30:19 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import numpy as np

vector = np.arange(0,50)
print(vector)

print(vector[::-1])

print(vector[40:33:-1])

print(np.arange(0,6).reshape(2,3))   #0 1 2 ---- 3 4 5
print(np.arange(0,50).reshape(2,25))
print(np.arange(0,10).reshape(5,2))

tresd=np.arange(1,82).reshape(3,3,3,3)
print(tresd)
print(np.random.random((3,3,3)))   

print(np.identity(6))  #matriz 6*6  matriz identidad 
print("otra forma para la matriz identidad ",np.eye(6))    #matriz identidad 


print(np.ones(6))
print("******")
print(np.ones((6,6)))
print(np.ones([6,6]))
print(np.random.random([3,3,3]))   





