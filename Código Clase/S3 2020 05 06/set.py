# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Fri May  6 17:33:52 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   [set]
# =============================================================================
# 
# =============================================================================
"""
#Check if "apple" is present in the fruits set.

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Use the remove method to remove "banana" from the fruits set

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
