# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Sat May 28 10:14:33 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [ejes3d]   [gráfico de superficie]
# =============================================================================
# 
# =============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np 
#from mpl_toolkits import mplot3d

datos_en_x=np.linspace(-5,5,100)
datos_en_y=np.linspace(-5,5,100)
print(datos_en_x)
X,Y=np.meshgrid(datos_en_x,datos_en_y)
Z= 1/(1+np.exp(-X-Y))
print(Z, type(Z))
print(X, type(X))
print(Y, type(Y))
fig=plt.Figure(figsize=(8,6))
ejes3d=plt.axes(projection="3d")
ejes3d.plot_surface(X,Y,Z,cmap="plasma")


plt.show()