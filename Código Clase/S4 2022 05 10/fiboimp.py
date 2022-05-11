# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 10 11:03:29 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""


import fibo;


fibo.fib(800)

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print("****")

print(fibo.fib2(100))

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print (fibo.__name__)

# 'fibo'

from fibo import fib, fib2
print(fib(500))
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import *
fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


from fibo import fib as fibonacci
fibonacci(500)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377



