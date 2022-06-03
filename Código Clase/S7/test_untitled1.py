# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Thu Jun  2 15:29:39 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""
import pytest
def suma (a,b):
        return a+b

print (suma(5,6))


def test_suma ():
    print("hola")
    assert suma(2, 3)==5
    
test_suma ()
print (test_suma ()) # esto da vacio

t=(
    "input_a, input_b, expected",
    [
     (3,4,7),
     (4,3,7),
     (suma(3,5),3,11),
     (3,suma(3,5),11)
    ]
)

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
     (3,4,7),
     (4,3,7),
     (suma(3,5),3,11),
     (3,suma(3,5),11)
    ]
)
def test_multi_suma (input_a, input_b, expected):
    assert suma(input_a, input_b)==expected
t=[
   (3,4,7),
   (4,3,7),
   (suma(3,5),3,11),
   (3,suma(3,5),11)
  ]

for i in t:
   #print(i[0],i[1],i[2])
   print(test_multi_suma (i[0],i[1],i[2]))
   