# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Tue May 31 19:23:08 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
try: 
    archivo = open("archivo de prueba.txt", "r")
    try:
        archivo.write("Esto es una nueva linea")
    except:
        print("Algo pasó al intentar escribir en el archivo")        
    finally:
        archivo.close()
except:
    print("Algo pasó al intentar abrir en el archivo")         
    