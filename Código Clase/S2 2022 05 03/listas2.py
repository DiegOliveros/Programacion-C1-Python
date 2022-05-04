# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May  3 19:45:53 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [listas 2]   [operaciones con listas]
# =============================================================================
# 
# =============================================================================
"""

lista_dos = ["Now", "we", "are", "coding","lists", "are"]
print(lista_dos)

for elemento in lista_dos:
    print(elemento)
print("\n")

lista_dos.pop(2)

for elemento in lista_dos:
    print(elemento)
    
print(lista_dos.index("lists",0,5))



