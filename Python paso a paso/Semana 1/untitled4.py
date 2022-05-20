# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:25:38 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

def pp(n):
    s = 0
    i = 1
    j = 1
    while (i <= n and j <= n):
        s = s + 1
        i = i + 1
        if i > n and j < n:
            i = 1
            j = j + 1
        
    
    print(s)
    
for i in range (0,50):
    pp(50)
