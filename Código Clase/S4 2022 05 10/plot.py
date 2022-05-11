# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 10 14:28:49 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [plot]
# =============================================================================
# numpy.arange
numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# =============================================================================
"""

from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()