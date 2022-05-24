# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 21 08:59:49 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

def suma(a):
    return a+1, a*8

print(suma(5))

for i in suma(5):   #recorro la tupla 
    print(i)        #imprime el valor de la tupla
    
    
    
variable=suma(5)
print(variable)  

def lista(a):
    resultado=[]     #declaro la lista
    for i in range(a):   #recorro un rango de 0 hasta el valor de a-1
        resultado.append(i)  #añado los valores a la lista
    return resultado

for i in lista(5):   #recorro la lista 
    print(i) 
    
print(lista(5))