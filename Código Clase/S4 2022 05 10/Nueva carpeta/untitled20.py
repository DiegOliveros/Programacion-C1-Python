# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 10 19:00:17 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [Fibonacci]
# =============================================================================
# 
# =============================================================================
"""
def fibonacci (n):
    a, b = 0,1
    while a<n:
        print (a, end=" ")
        a, b =b, a+b
        
        
def fibonacci_list (n):
    a, b = 0,1
    resultado =[]
    while a<n:
        resultado.append(a)
        a, b =b, a+b
    print(resultado)
    
fibonacci(100)
print("\n")
fibonacci_list(100)



# n=1000
# a, b = 0,1
# 
# while a<n:
#     resultado.append(a)
#     # print (a, end=" ")
#     a, b =b, a+b
# print("\n")
# print(resultado)