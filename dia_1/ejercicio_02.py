# Importamos las funciones
from funciones_02 import  get_number, suma, resta

#Guardamos los datos en las variables
first_number, second_number = get_number()

#hacemos las operaciones
Suma = suma(first_number, second_number)
Resta = resta(first_number, second_number)


numero_dado = 10

if Suma > numero_dado:
    print(f"La suma de {first_number} y {second_number} es mayor a {numero_dado}")
else: 
    print(f"La suma de {first_number} y {second_number} es menor a {numero_dado}")