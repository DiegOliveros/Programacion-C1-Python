# ******** SEMANA 3 ***********
# 
# Diego Iván Oliveros Acosta @scalapp.co   
# 
# lista.py comenzando con listas en Python 

x=["Now", "we", "are", "cooking!"]
type(x)
print(x)
# ['Now', 'we', 'are', 'cooking!']
print(len(x))
#4
print("are" in x)
#True
print("today" in x)
#False
print(x[0])
#Now
print(x[3])
#cooking!
# print(x[4])
#IndexError: list index out of range
print(x[1:3])
# ['we', 'are']
print(x[2:])
#['are', 'cooking!']
print(x[:2])
#['Now', 'we']
fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")
print(fruits)
# ['apple', 'banana', 'cherry', 'kiwi']
fruits.insert(0,"orange")
print(fruits)
#['orange', 'apple', 'banana', 'cherry', 'kiwi']
fruits.insert(0,"orange")
print(fruits)
# ['orange', 'orange', 'apple', 'banana', 'cherry', 'kiwi']
# fruits.remove("Melon")
print(fruits)
# ValueError: list.remove(x): x not in list
# fruits.remove("Pear")
print(fruits)
# ValueError: list.remove(x): x not in list
fruits.pop(3)
print(fruits)
# "apple"
print(fruits)
fruits[2]="Strawberry"
print(fruits)
# ['orange', 'orange', 'Strawberry', 'cherry', 'kiwi']












