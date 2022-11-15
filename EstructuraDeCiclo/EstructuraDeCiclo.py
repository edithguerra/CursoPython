#LOS CICLOS O BUCLES EN PYTHON
#los ciclos, tambien conocidos como bucles o estructuras de control repetitivas, son de total importacia para
#el proceso de creacion de un programa. Un ciclo en Python o bucle en Python te permite repetir una o varias
#intrucciones cuantas veces lo necesites, por ejemplo, si quisieramos escribir los numeros del uno al cien
#no tendria sentido escribir cien lineas de codigo mostrando un numero en cada una, para eso y varias cosas mas
#es util un ciclo. Un ciclo nos ayuda a llevar a cabo una tarea repetitiva en una cantidad de lineas muy
#pequeñas y de forma practicamente automatica(y muy rapida).

#Existen diferentes tipos de ciclos o bucles en Python, cada uno tiene una utilidad para casos especificos y
#depende de nuestra habilidad y conocimientos poder determinar en que momento es bueno es usar uno de ellos.
#Tenemos entonces a nuestra disposicion los siguientes tipos de ciclos en Python:
# °Ciclo while en Python.
# °Ciclo for en Python.
for contador in range (1,11,1):
    print(contador)
#_CLASE_
# while tambien es una estructura de ciclo
# int es metodo de Python quen transforma un dato tipo texto a tipo numerico real o entero.
# input es un metodo de Python que pide un dato por consola al usuario.
condicion=True
while condicion==True:
    numero=int(input('ingresa el numero ganador'))
    if numero==10:
       print('ganaste el premio')
       condicion=False
    else:
        print('no eres el ganador')
#TAREA
#CREAR UN PROGRAMA QUE ME PIDA MI EDAD, SI INGRESO UNA EDAD INCORRECTA EL PROGRAMA SEGUIRA PIDIENDO MI EDAD
#SI ES LA EDAD CORRECTA ME MOSTRARA UN MENSAJE DE CORRECTO Y SE TERMINARA LA EJECUCION.
Edad=True
while Edad==True:
    numero=int(input('ingresa el numero de la edad'))
    if numero==20:
       print('edad correcta')
       Edad=False

password='71439017'
for intentos in range(1,4):
    print('este es tu',intentos,'intento')
    newPassword=input('ingresa el password correcto:')
    if newPassword==password:
        print('bienvenido al sistema joven')
        break
    else:
        print('password incorrecto sigue intentando')

##tabla d multiplicar del 1 al 10
for tabla in range(0,11):
    print('tabla del', tabla)
    for num in range(11):
        print(tabla, 'x', num,'=',tabla*num)

##tabla d multiplicar del 1 al 10
evaluar=True
while evaluar==True:
  numero=int(input('ingrese el numero de la tabla'))
  if numero==0:
      print('saliendo del programa')
      break
for numeros in range (1,11):
    print(numeros,'x',numero,'=' ,numeros*numero)

mensaje='hola'
print(mensaje[3])
for letra in mensaje:
    print (letra)
##print(mensaje[3])

mensaaje=(input('ingrese un mensaje'))
#mostrar por consola cuantas vocales 'a' tiene el mensaje
for letra in mensaje:
    print(letra)


##clase 07/11/2022
mensajeOpciones="""
===================
selecciona una opcion
 1)suma 
 2)resta
 3)division
 4)multilplicacion
 5)salir
===================
"""
while True:
    print (mensajeOpciones)
    opcion=input('ingresa una opcion valida entre (1-5):')
    numeroUno=int(input('ingresa el primer numero'))
    numeroDos=int(input('ingresa el segundo numero'))
    match opcion:
        case '1':
            print(f'la suma de{numeroUno}+{numeroDos}={numeroUno + numeroDos}')
        case '2':
            print(f'la resta de{numeroUno}-{numeroDos}={numeroUno - numeroDos}')
        case '3':
            print(f'la multiplicacion de{numeroUno}*{numeroDos}={numeroUno * numeroDos}')
        case '4':
            print(f'la division de{numeroUno}/{numeroDos}={numeroUno / numeroDos}')
        case '5':
            break
        case __:
            print('esta opcion no existe')


##practica
numero = int(input('ingresa el numero de una opcion 1=suma 2=resta 3=multiplicacion 4=division'))
numero1 = int(input('ingresa el primer numero '))
numero2 = int(input('ingresa el segundo numero '))
if numero==1:
        suma = numero1 + numero2
        print('el resultado es',suma)
elif numero==2:
        resta = numero1 - numero2
        print('el resultado es',resta)
elif numero==3:
        multiplicacion = numero1 * numero2
        print('el resultado es',multiplicacion)
elif numero ==4:
        division = numero1 / numero2
        print('el resultado es',division)
else:
         print('salir')
numero = True
while numero == True:
   otraOpcion = int(input('ingresa otra opcion'))