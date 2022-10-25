#AVERIGUAR SOBRE FUNCIONES
#Las funciones de Python contituyen unidades logicas de un programa y tienen un doble objetivo:
# °Dividir y organizar el codigo en partes mas sencilla.
# °Encapsular el codigo que se repite a lo largo de un programa para ser reutilizado.
#La funcion len(),que obtiene el número de elementos de un objeto contenedor como una lista,
#una tupla, un diccionario o un conjunto.
# la función print(), que muestra por consola un texto.

#Para usar o invocar a una función, simplemente hay que escribir su nombre como si de una
#instrucción más se tratara. Eso sí, pasando los argumentos necesarios según los
#parámetros que defina la función.
#VAMOS A CREAR UNA FUNCION QUE MUESTRA POR PANTALLA EL RESULTADO DE MULTIPLICAR UN NUMERO CINCO
def multiplica_por_5(numero):
 print('comienzo del programa')
 print(f'{numero} * 5 = {numero * 5}')
multiplica_por_5(7)
print('siguiente')
multiplica_por_5(113)
print('fin')

#2 tipos de funciones
#FUNCIONES PROPIAS DE PYTHON
print()#sirve para mostrar mensajes o resultados.
int()#esta funcion sirve para convertir string en entero.
input()#esta funcion sirve para pedir datos al usuario

#FUNCIONES CREADAS
#creando funcion hola
def saludo():
    return "hola"
#usom de funcion
print(saludo())

#escfribir un programa que muestre el eco de todo lo que el usuario introdustca hasta que el
#usuario escriba  'salir' para terminar la ejecucion
palabra=''
while palabra!='salir':
    palabra=input('escriba una palabra:')
    print(palabra)

#con for
contador=0
for num in range(0,contador):
    palabra = input('ingresa una palabra:')
    if palabra=='salir':
        break
    contador+=1

#otra manera
sentence=input('ingrese una oracion: ')
sentence2=input('ingrese otro texto: ')
def countVocals(texto):
    vocales=['a','e','i','o','u']
    contadorVocales=0
    for letras in texto:
        if letras in vocales:
            contadorVocales+=1
    return contadorVocales
print('la cantidad de vocales es:', countVocals(sentence))
print('la cantidad de vocales es:', countVocals(sentence2))

#ejercicios
def mensaje(nombre,apellido,accion):
    if accion=='saludo':
        mensaje='hola' ,nombre ,apellido, 'como estas'
    elif accion=='despedida':
        mensaje='adios' ,nombre ,apellido
    return mensaje
print (mensaje('Edith','Guerra','despedida'))

#forma 2
sentece=input('enter sentence:')
vocales=['a','e','i','0','u']
def countvocal(oracion,vocal):
    contador=0
    for word in oracion:
        if word in vocal:
            contador+=1
    return contador
print(countvocal(sentece,vocales))
