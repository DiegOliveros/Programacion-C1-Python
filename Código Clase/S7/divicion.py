# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Thu Jun  2 19:18:45 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [divide.py]   
# =============================================================================
# [Tomar dos argumentos x , y para luego dividirlos]
# =============================================================================
"""

def f_divide1(x,y):
     """ 
     Tomar dos argumentos x , y 
     para luego dividirlos sin controlar la divisiòn por 0
     """
     c=x/y
     return c   #sería lo mismo que solo retornar x+y
 
    
def f_divide2(x,y):
     """ 
     Tomar dos argumentos x , y para luego dividirlos
     controlando la diviciòn por 0
     """
     if y ==0:
         return "no es poible realizar diviciòn por 0"
     c=x/y
     return c   #sería lo mismo que solo retornar x+y
 
    
def f_divide3(x,y):
     """ 
     Tomar dos argumentos x , y para luego dividirlos
     controlando la diviciòn por 0 
     """
    
     try: 
         c=x/y #no se ejecuta cuando es divición por 0
     except ZeroDivisionError:
         print( "no es poible realizar diviciòn por 0")
     except UnboundLocalError:
         c=None    #esta linea nunca se ejecuta 
         return c  #esta linea nunca se ejecuta
     return c   #sería lo mismo que solo retornar x+y 
                #el error se produce cuando retorno c 
                #porque se no tiene valor en caso de div por 0
                
print(f_divide2(5,0))
print(f_divide1(5,5))
print(f_divide3(7,5))
 
try: 
    f_divide3(7,0)
except UnboundLocalError:
    print("la variable c no tiene un valor asignado")

print(f_divide3(7,5))



