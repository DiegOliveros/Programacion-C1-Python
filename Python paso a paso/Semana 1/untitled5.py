# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:29:04 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

V = [20, 3, 1, 6, 2, 7, 4, 9, 5, 2, 1, 9, 8, 3, 1, 5, 9, 3, 5, 6, 8]
n = len(V)
k = 1
j = 1
for i in range(1, n):
    if V[i] < V[k]:
        k = i
    if V[i] >= V[j]:
        j = i
print(j, k)