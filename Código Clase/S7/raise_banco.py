# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Tue May 31 19:38:01 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [raise]   [creando mis propias excepciones]
# =============================================================================
# Para casos en los cuales quiero terminar el prograna 
una transacción bancaria 
# =============================================================================
"""

número_intentos =4

if número_intentos >=3:   #si son 3 o más debe lanzar la excepción 
    raise Exception("ha excedido el número de intentos de clave")
    
usser="Roberto"

if not type(usser) is int:
    raise TypeError("los usuarios solo pueden tener nominación en entero")