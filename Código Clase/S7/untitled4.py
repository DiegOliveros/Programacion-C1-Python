# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Sat Jun  4 10:14:26 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

universidad = {
     
    "Pensum":[2021,2022,2023],
    "materia":{2021:["Física", "Biología","Java", "Anatomía y fisiología", "Matemáticas", "Química", "Ecología"],
              2022:["programación", "java*","análisis", "requisitos ", "ética","Biología"],
              2023:["Ingles", "Logica Matematica*", "Java", "Habilidades "]
        },
    "pre-requisitos":[(1,5),(7,9)],
    "semestre":{2021:[1,1,2,2,3,3],
              2022:[1,2,2,3],
              2023:[1,1,3,3]},
    "creditos":{2021:[1,4,8,2,3,1],
                2022:[1,1,1,1],
                2023:[1,2,4,3]}
    }

# print(universidad)
print("las claves de las materias son:\n")
for i in universidad["materia"].keys():
    print(i)

print("\n\nlos valores de las materias son:")

for i in universidad["materia"].values():
    print(i)
    
#recorrido de los valores de las listas
    
for i in universidad["materia"].values():
    for x in i:
        print(x.lower())
for i in universidad["materia"].values():
    for x in i:
        print(x.upper())
        
        
contador={}
contador["java"] =0

for i in universidad["materia"].values():
    for x in i:
        # (x.replace("í","")).lower())
        if (x.replace("*","")).lower() =="java":
           contador["java"] +=1 

print(contador)


