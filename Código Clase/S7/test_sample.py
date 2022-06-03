# -*- coding: utf-8 -*-
"""
# ******** SEMANA 7 ***********
Created on Thu Jun  2 16:07:32 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [incremento.py]   []
# =============================================================================
# Realizar un programa que ingremente y revisar el paso de prueba
pip install -U pytest
conda install -c spyder-ide spyder-unittest
$ pytest --version
pytest 7.1.2
# =============================================================================
"""


def incremento(x):
    return x + 1


def test_incremento():
    assert incremento(3) == 4