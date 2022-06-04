# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Sat Jun  4 09:08:22 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
import random 

secreto =random.randint(0,100)

intentos=1

while intentos<=6:
    intentos+=1  #intentos=intentos+1
    
    numero=-2
    while not (-1<numero<101):
        try:
            numero=int(input("ingrese un número entre 0 y 100"))
        except ValueError:
            print("No es un número, ingrese un número")
        if not (-1<numero<101):
            print("El número está fuera de rango (0 a 100)")
    
    if numero<secreto:
        print("El número es menor que el secreto")
    elif numero>secreto:
        print("El número es mayor que el secreto")
    
    else: # if numero==secreto:
        print("Lo lograste! en "+ str(intentos-1) + " intento")
        intentos=6
        break
    
if intentos>6:
    print("Lo lamento fallaste")
    print("el número secreto es: "+ str(secreto))
    
    
    

       