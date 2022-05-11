# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 10 11:00:56 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [fibo.py]
# =============================================================================
# 
# =============================================================================
"""

# Fibonacci numbers module

def fib(fib):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < fib:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))