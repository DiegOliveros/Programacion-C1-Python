# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:24:39 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

V = [5, 0, 0, 0, 0, 0, 0, 0, 0, 4, 9, 1, 4, 1, 2]
for i in range(V[0] + 1, 15):
    print(V[i], end="")
print(end="...")
i = V[0]
while V[i+1] == 0:
    V[0] = V[0] + 1
    i = i + 1
for i in range(V[0] + 1, 15):
    print(V[i], end="")