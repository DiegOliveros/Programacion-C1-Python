file = open("archivoprueba.txt","r")
print(file.read())  #texto compleo 


print(file.read(132))  #Número de caracteres 
file = open("archivoprueba.txt","r")
print("Una línea: \n",file.readline())  
print("dos línea: \n",file.readline())  


#presentar una sola línea 

print(file.read(132))  #Número de caracteres 
file = open("archivoprueba.txt","r")
file.readline()
file.readline()

print("tres línea: \n",file.readline())  

archivo = open("archivoprueba.txt","r")

for i in archivo:
    print(i)
    
archivo.close()