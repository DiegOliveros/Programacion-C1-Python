# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:25:02 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

def misterio(V, i, n):
    if i < n:
        misterio(V, 2*i+1, n)
        print(V[i], end=",")
        misterio(V, 2*i, n)
V = [8, 3, 1, 6, 2, 7, 4, 9, 5]
misterio(V, 1, 9)