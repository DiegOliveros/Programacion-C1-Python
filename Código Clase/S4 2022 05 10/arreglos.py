# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 14 08:10:33 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
import numpy as modulo #np por lo general pero puede ser cualquiera 
arreglo=modulo.array(["a","b"])
print(arreglo)
arreglo=modulo.array([["a","b"],["a","b"]])
print(arreglo)
arreglo=modulo.array([("a","b"),("a","b")])
print(arreglo)

arreglo=modulo.array([(1.5,2.0,8),(4,55,2.5)], dtype=float)
print(arreglo)
print(modulo.info(modulo.ndarray.dtype))
print(type(arreglo))
print(type(arreglo[1][1]))

arreglo=modulo.array([(1.5,2.0,8),(4,55,2.5),(0,55,2.5)], dtype=float)
print(arreglo)

