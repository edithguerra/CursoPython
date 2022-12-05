#definir una funcion max() que tome como argumento un array de numeros y devuelva el mayor del array


#escribir una funcion que alamacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y
#muestre por pantalla el menor y el mayor de los precios.
precio=[50,75,46,22,80,65,8]

#escribir una funcion mas_larga() que tome un array de palabras y devuelva la mas larga

def mas_larga(lista):
    mas_larga=''
    for i in lista:
        if len(i)> len(mas_larga):
            mas_larga=i
            return mas_larga

print (mas_larga)

#escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene