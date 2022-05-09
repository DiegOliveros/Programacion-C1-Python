# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat May  7 09:06:25 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

secuencia ={"manzana", "banano", "pera",8,0, True, False}


# secuencia.add([1,2])   no se permite 
# print(secuencia)

secuencia ={"manzana", "banano", "pera",8,0, True, False}
secuencia.add("naranja")
print(secuencia)

conjunto ={"mango","uva","melocotón"}

# secuencia.update(conjunto)

# print("forma 1",secuencia)

secuenciaconunion=secuencia.union(conjunto)

print("forma 2",secuenciaconunion)


numeros ={1,2,3,4,5}
letras={"a","b","c","d"}

numeros.update(letras)
print("el conjunto numeros final es:", numeros)

secuencia.remove("manzana") # si el elemento no existe me genera error
print("utilizando remove:", secuencia)
secuencia.discard("mango")
print("utilizando dicard:", secuencia) #NO importa si no existe 
secuencia.discard("banano")
print("utilizando dicard:", secuencia) #si existe lo borra 
secuencia.pop()
print("utilizando pop:", secuencia) #NO tengo control de cuál elimina

secuencia.clear()

print("utilizando clear():", secuencia) #vacía el contenido del conjunto

del secuencia
#print("utilizando clear():", secuencia) #vacía el contenido del conjunto

