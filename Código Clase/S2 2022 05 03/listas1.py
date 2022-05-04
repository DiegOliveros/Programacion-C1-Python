# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May  3 19:08:31 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [listas 1]   [sintaxis listas]
# =============================================================================
# 
# =============================================================================
"""

lista_uno = [1,2,9,5,9]
print(type(lista_uno))
print(lista_uno)

lista_dos = ["Now", "we", "are", "coding","lists", "are"]
print(lista_dos)

for elemento in lista_dos:
    print(elemento)
    
print("longitud de lista uno y dos:",len(lista_uno),len(lista_dos))

lista_tres =["1","1.5","hola mundo",1,5.5]
print(lista_tres) 


print('Lista tres tiene "are"?',"are" not in lista_tres,9*52)
print('Lista dos tiene "are"?',"are" in lista_dos, 1+2)

print("el resultado con count",lista_dos.count("are"))
print("el resultado con count",lista_dos.count("hola"))

print("el elemneto 4 de la lista dos es:", lista_dos[3], "y se encuentra en: ", 
      lista_dos.index("coding"))
print(lista_dos[5])
#print(lista_dos[6]) IndexError: list index out of range
# =============================================================================
# LTERANDO LA LISTA
# =============================================================================

lista_dos[0] ="very good!"

for elemento in lista_dos:
    print(elemento)

lista_dos.insert(0, "Now")

for elemento in lista_dos:
    print(elemento)
    
    
    







