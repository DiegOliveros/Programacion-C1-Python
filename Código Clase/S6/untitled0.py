# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 31 16:39:51 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

try:
  print(x)
except NameError:
  print("La variable x no está definida")
except:
  print("Algo más salió mal ")
  
  
try:
  print("Hola mundo")
except:
  print("Algo más salió mal ")
else:
  print("Nada salió mal ")
  
  
try:
  print(x)
except:
  print("Algo más salió mal ")
finally:
  print("la claula 'try except' ha finalizado")
  
  
x = -1

if x < 0:
  raise Exception("Lo lamento no se admiten números bajo 0")