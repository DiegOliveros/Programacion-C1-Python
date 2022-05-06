# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Thu May  5 18:26:04 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
#declarando un diccionario
diccionario = {"unaclavequeNOexiste":10, "cadena2":[1,2,3,4],"cadena3":10,"clave":"valor"}
print(diccionario)
#llamando un solo elemento 
print(diccionario["cadena2"])
#preguntar por una clave
print("clave" in diccionario)
print("unaclavequeNOexiste" in diccionario)
print("realizo una operación sobre un valor:")

a=diccionario["unaclavequeNOexiste"]
print(a*10)    #Son lo mismo que: print(diccionario[unaclavequeNOexiste]*10)

diccionario2 = {
    "1":[15,"Rafael","Medellín"],
    "2":[28,"Juan", "password"],
    "3":[10,"Ana"],
    "Pablo":10}
print("1" in diccionario2)