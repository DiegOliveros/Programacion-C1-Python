# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 31 19:03:51 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""


# x=1
# print(x/0)

try:
    print(x)

except NameError: 
    print("ocurrió un falla por variable no definida")

try: 
    x=1
    # print(x/0)
    
except ZeroDivisionError: 
    print("ocurrió un falla por división por 0")

except:
    print("tenemos un error")
else:
    print("Nada salió mal, todo salió bien")
    
finally:
    print("esto sería un mensaje final que siempre se ejecuta")
    print("independiente si las excepciones de dan")

    
    
    
    
    
    
    
    