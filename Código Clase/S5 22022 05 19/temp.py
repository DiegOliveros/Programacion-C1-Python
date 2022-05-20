import random   #importo la libreria 
#hola   #0121 #hala #hola #holo
#crear una lista de tamaño 4 y 
#llenarla con 4 números aleatorios 
# sin repetir valores. 
def flistaaleatoria():
    listaaleatoria=[]
    for i in range (0,4): #generar el número aleatorio
        numero_aleatorio = random.randint(0,3) #print(numero_aleatorio)
        #mientras que el número esté en la lista genere un aleatorio
        while numero_aleatorio in listaaleatoria:#ver que no esté en la lista 
            numero_aleatorio = random.randint(0,3)
        listaaleatoria.append(numero_aleatorio)  #guardar en la lista 
    return listaaleatoria
   
# h = 0   
# o = 1
# l = 2  
# a = 3


def encriptar(cadena):
    cadena.lower()  #poner todas las letras en minúscula
    cadenasif=[0,0,0,0]  
    for i in cadena:
        if i == cadena[0]:  #h
            cadenasif[0]=lista_a[0]
        if i == cadena[1]:  #o
            cadenasif[1]=lista_a[1]
        if i == cadena[2]:  #l
            cadenasif[2]=lista_a[2]
        if i == cadena[3]:  #a
            cadenasif[3]=lista_a[3]
    return cadenasif          
#     cadenacifrada=cadenacifrada+"0



def desencriptar(listacifrada, lista_a,cadena):
    cadenasif=["","","",""]
    for i in listacifrada:
        if i == lista_a[0]:  #código secreto 
            cadenasif[0]=cadena[0]  #la representación guardada
        if i == lista_a[1]:
            cadenasif[1]=cadena[1]
        if i == lista_a[2]:
            cadenasif[2]=cadena[2]
        if i == lista_a[3]:
            cadenasif[3]=cadena[3]
    
    return cadenasif
lista_a=flistaaleatoria()

print("la lista aleatoria 1 es: ", lista_a)
listaencriptada1=encriptar("hola")
print("la lista encriptada 1 es:",listaencriptada1)
print("la lista desencriptada 1 es:",desencriptar(listaencriptada1,lista_a,"hola"))

lista_a=flistaaleatoria()
print("la lista aleatoria 2 es: ", lista_a)
listaencriptada2=encriptar("hola")
print("la lista encriptada 2 es:",listaencriptada2)
print("la lista desencriptada 2 es:",desencriptar(listaencriptada2,lista_a,"hola"))