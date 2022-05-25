# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 24 18:09:22 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\ITOS\\Documents\\GitHub\\Programaci-n-C1-Grupo-9-\\Bases de datos\\twitter.csv", sep=";")
print(df.to_string())