# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 14 10:48:19 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import pandas as pd

df=pd.read_csv("./atleta2.csv")
print(df.to_string()) #todo el archivo 

print(df.head(5))   #los 5 primeros 

print(df.tail(5))   #los 5 ultimos 


print(df.describe())   #los 5 primeros 

