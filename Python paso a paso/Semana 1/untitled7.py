# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:30:29 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

V = [10, 3, 1, 6, 2, 7, 4, 9, 5, 2, 1, 9, 8, 3, 1, 5, 9, 8, 5, 6, 3]
i = 1
j = V[0]
while i < j:
    while i <= V[0] and V[i] % 2 == 1:
        i = i + 1
    while j > 0 and V[j] % 2 == 0:
        j = j - 1
    if i < j:
        a = V[i]
        V[i] = V[j]
        V[j] = a
for i in range(1, len(V)):
    print(V[i], end = ", ")