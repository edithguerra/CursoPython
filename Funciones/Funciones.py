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

#TAREA
##crear una funcion de operadores aritmeticos matematicos
def suma(a,b):
    resultado = a+b
    return resultado
print(suma(5,6))
def resta(a,b):
    resultado = a-b
    return resultado
print(resta(10,6)) 
def division(a,b):
    resultado = a/b
    return resultado
print(division(10,2))
def multiplicacion(a,b):
    resultado = a*b
    return resultado
print(multiplicacion(5,6))


##TAREA 'todo lo de match en una funcion' #operacion(numero1,numero2,operando#
numeroUno=int(input('ingresa el primer numero'))
numeroDos=int(input('ingresa el segundo numero'))
def suma(numeroUno,numeroDos):
    resultado = numeroUno+numeroDos
    return resultado
print(suma(numeroUno,numeroDos))
def resta(numeroUno,numeroDos):
    resultado = numeroUno-numeroDos
    return resultado
print(resta(numeroUno,numeroDos))
def division(numeroUno,numeroDos):
    resultado = numeroUno/numeroDos
    return resultado
print(division(numeroUno,numeroDos))
def multiplicacion(numeroUno,numeroDos):
    resultado = numeroUno*numeroDos
    return resultado
print(multiplicacion(numeroUno,numeroDos))


##clase del 08/11/2022
#1. UTILIZAR LA PALABRA RESERVADA def
#2. asignamos un nombre a la funcion--descriptivo
#3. siempre tiene que recibir parametros
  # ()--no resive parametros
  # (nombre)--que la funcion esta recibiendo un parametro
  # (edad,nombre)
#4.siempre la funcion tiene que retornar un tipo de dato
def saludo():
    respuesta='hola como estas'
    return respuesta
  #como uso
  arrayAmigos=['ronal','claudio','diego','jose','edith']
for amigo in range(0,len(arrayAmigos)):
      print(saludo(arrayAmigos[amigo]))

#    TAREA
# crear una funcion que me retorne los n numeros fibonacci
def numeros(n):
    if n < 2:
        return n
    else:
        return numeros(n-1)+numeros(n-2)
for x in range(10):
    print(numeros(x))

# crear una funcion que me retorne el factorial de un numero n
def factorial(*n):
    for x in n:
        fac=1
        for Y in range (1,x+1):
            fac=fac*Y
            print(fac)
factorial(5)

# crear una funcion que me diga  si una palabra es palindromo
texto =input('ingrese la palabra: ')
revertido = texto [::-1]
if texto == revertido:
    print('lampalabra ingresada si es palidromo')
else:
    print('lampalabra ingresada no es palidromo')

##clase
def operaciones(num1,num2,operador):
    if operador=='suma':
        total=num1+num2
    if operador == 'resta':
        total = num1 - num2
    if operador == 'multiplicacion':
            total = num1 * num2
    if operador == 'division':
                total = num1 / num2
                return total
# llamando la funcion
print(operaciones(10,8,'resta'))
print(operaciones(100,20,'sumar'))
#palabras reservadas para unir archivos (import)
import funciones as op--#alias