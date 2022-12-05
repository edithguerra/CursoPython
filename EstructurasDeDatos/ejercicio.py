##escriba una funcion en python que acepte una lista y genere otra lista eliminando los duplicados
def delDuplicate(array):
    newArray=[]
    for el in array:
      if el not in newArray:
        newArray.append(el)
    return newArray
arrayD=[2,2,5,5,1,4,7,6]
print(delDuplicate(arrayD))
##escriba una funcion en python que acepte una lista y genere otra con los numeros pares
def numPar(array):
    newArray=[]
    for i in array:
      if i%2==0 not in newArray:
        newArray.append(i)
    return newArray
arrayD=[2,2,5,5,1,4,7,6]
print(numPar(arrayD))
##escriba una funcion en python que acepte una lista y genere otra eliminando los duplicados texto
def stringDuplicate (array):
    newArray=[]
    for el in array:
        if el not in newArray:
            newArray.append(el)
    return newArray
arrayD =['a', 'a', 'b', 'c', 'c', 'd', 'e', 'f', 'f']
print(stringDuplicate(arrayD))
#TAREA
##escriba una funcion en python que acepte una lista y genere otra que muestre los numeros primos
def es_primo(num):
    newArray=[]
    for n in num:
        if num%n != 0 not in newArray:
            newArray.append(n)
    return newArray
arrayD=[1,2,3,4,5,6,7,8,9,10]
print(numPar(arrayD))






