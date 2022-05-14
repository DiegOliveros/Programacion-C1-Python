# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 14 09:56:04 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,20,True)
y=np.linspace(0,10,20)

# plt.plot(x,y,'purple') 
# plt.plot(x,y,'o') 

# x = np.array([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1],
# [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]], np.float64)
# y = np.array([[-7.4], [-2.3], [3], [7.6], [12.0],
# # [17.9], [22.5], [27.6], [32.1], [37.4]], np.float64)
# x=np.arange(0, 5, 1, dtype=int)
# y=np.arange(0,5,1, dtype=float)

print(x)
print(y)
plt.plot(x,y,'purple') 
plt.plot(x,y,'o') 