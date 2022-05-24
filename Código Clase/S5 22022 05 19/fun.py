# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May 21 08:23:03 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

def funcion():  #función sin retorno y sin parámetros 
   a=1+2
        
variable=funcion()
print(variable)

def funcion2(param1, param2):
    suma=param1+param2
    return suma

def funcion3(param1):  #función con retorno y con parámetro 
    param1+=1
    return param1    


def funcion():  #función con retorno y sin parámetros 
  #
    return 1+2


def funcion_recur(parm):  #función con retorno y sin parámetros 
    parm+=1
    print(parm)
    if parm<3:
        funcion_recur(parm) #llamado a la función
        
    return parm


print(funcion2(5,8))  # 5 y 8 son los argumentos de la función 
print(funcion2(8,8))
print(funcion2(9,8))

print(funcion3(funcion2(1,2)))   


print(funcion_recur(-50))


def multiploca_por_5(numero):  #definición de la función 
    print("\t",numero,"* 5 =", numero*5)
    print(f"\t {numero} * 5 = {numero*5}")
    
    
print("comienzo del programa\n")
multiploca_por_5(35) #ejecutar la función 
multiploca_por_5(1) #ejecutar la función 
multiploca_por_5(2) #ejecutar la función 
multiploca_por_5(3) #ejecutar la función 







