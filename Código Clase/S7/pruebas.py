# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Fri Jun  3 17:43:09 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/DiegOliveros/Programacion-C1-Python/main/C%C3%B3digo%20Clase/S4%202022%2005%2010/atleta2.csv", sep=",") # separadores "|" "," ";" ":" 
                                                 # "t"o "\t" =no es el simbolo t sino que es un tabulador "tab" 
print(df.to_string()) #todo el archivo 
print(df.head(5))   #los 5 primeros 
print(df.tail(5))   #los 5 ultimos 
print(df.describe())   #los 5 primeros 
print(chr(104))
print(ord('h'))
s = input("ingrese un valor: ")
l1=[c for c in s]   
l2=[ord(c) for c in s]
print(l1)
print(l2)
print(df["     Duration "][5])
print(df[" Calories"])
#df["     Duration "][5]=1985
print(df["     Duration "][5])
def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new
      
      
# driver code   
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))



import pandas as pd
import numpy as np

data = {'name':['michael','louis','jack','jasmine'],
       'city':['berlin','paris','roma',np.nan]}
df = pd.DataFrame(data,columns=['name','city'])
#/replace column values with function

df['city']=df['city'].map('I am from {}'.format)

print(df)