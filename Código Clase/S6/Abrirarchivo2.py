# -*- coding: utf-8 -*-
"""
# ******** SEMANA 6 ***********
Created on Tue May 24 18:38:55 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

file = open("archivoprueba4.txt","a")  #agregar y si no existe, crea y agrega 
file.write("\nEsto es una línea adicional")
file.close()

file = open("archivoprueba4.txt","r")   #leer
print(file.read())  #texto compleo 
file.close()    #importante para borrar o ver los cambios