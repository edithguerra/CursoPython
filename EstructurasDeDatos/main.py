##estructra de datos
##listas
##metodos para estructuras de datos tipo lista en python
#list=[]--> lista vacia
list=['deyanira']#lista vacia
list.append('diego')
list.insert(0,'edith')
list.insert(len(list),'jamely')
print(list)

#lista de 10 numeros
list=[]
for i in range(11):
    list.append(i)
print(list)

#numeros pares entre 2 y 20
list=[]
for i in range(21):
    if i%2==0:
        list.append(i)
print(list)

##para unir listas y actualizar un dato y quitar
vocalesUno=['a','e']
vocalesDos=['i','o','u']

vocalesUno.extend(vocalesDos)
vocalesUno[3]='00'
vocalesUno.remove('u')
print(vocalesUno)