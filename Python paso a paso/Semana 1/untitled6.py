# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May 19 15:29:14 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

mat = [[3, 1, 6, 2], [7, 4, 9, 5], [2, 1, 9, 8], [3, 1, 5, 9], [3, 5, 6, 8]]
s = 0
for i in range (1, 5):
    for j in range(1, 4):
        s = s + mat[4-i+1][3-j+1]
print(s)