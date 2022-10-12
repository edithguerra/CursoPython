#ESTRUCTURA DE DECISION
#Varias sentencias de Python permiten al programador especificar de siguiente sentencia a ser ejecutada puede
#ser otra diferente  de la siguente en secuencia. Esto es llamado transferencia de control. la transferencia
#de control. La transferencia de control se logra con las estructuras de decision de Python.
#  IF
#Las estructuras de decision escogen entre difernetes cursos de accion. Por ejemplo, suponga que la nota para
#aprobar un curso en 16. La sentencia en pseudocodigo es la siguiente:
#si el estudiante obtine una nota igual o superior a 16: Aprovado
#Si la condicion es verdadera; se imprime "Aprovado". Si la condicion es falsa, la sentencia de impresion
#es ignorada. Escrito en python se veria dr la siguiente manera:
nota=17
if nota >=16:
   print ("Aprovado")
#  IF/ELSE Y IF/ELIF/ELSE
#La estructura de decision if realiza una accion especifica solo cuando la condicion es verdadera; de lo
#contrario, la accion se ignora. la estructura if/else permite al programador especificar que una accion
#diferente se debe desarrollar, cuando la condicion es falsa. Por ejemplo, la sentencia en pseudocodigo:
#si el estudiante obtine una nota igual o superior a 16:
#entonces: Aprovado
#si no: Suspendido
#Escrito en Python:
if nota >= 16:
    print("Aprovado")
else:
    print("Suspendido")
#Tambien se utiliza la estructura de seleccion multiple if/elif/else. Que se veria en Python de la siguiente
#manera:
if nota >= 16:
    print("A")
elif nota >= 15:
    print("B")
elif nota >= 14:
    print("C")
elif nota >= 13:
    print("D")
else:
    print("F")








