# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Thu Jun  2 18:46:55 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [test_suma]   []
# =============================================================================
# 
# =============================================================================
"""
#lo primero es remplazar esa forma 
#de probar por el archivo de prueba 
# def suma(x,y):
#     """ 
#     Tomar dos argumentos x , y para luego sumarlos
#     """
#     return x+y

#algunas pruebastradicionales 

#Estructura de una prueba 
import pytest
from suma import suma

def test_suma():
    assert suma(2,5) ==7
    assert suma(3,5) ==8

def test_suma2():
    assert suma(3,5) ==8



# lista_pruebas=[
#     (2,5,7),
#     (3,5,8),
#     (suma(3,5),3,11),
#     (3,suma(3,5),11)
#     ] 

# print(lista_pruebas)

@pytest.mark.parametrize(
    "input_a,input_b,esperado",
    [   (2,5,7),   #
        (5,2,7),
        (suma(3,5),3,11),
        (3,suma(3,5),11)
    ] 
)
def test_multiple_suma(input_a,input_b,esperado):
    assert suma(input_a,input_b)==esperado
    
    
# for i in lista_pruebas:
#     test_multiple_suma(i[0],i[1],i[2])



