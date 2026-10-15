
from funciones_ejercicio1 import get_option, get_number, suma, resta, multiplicacion, division

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

while True :

    print ('''Elige la operacion que vas a realizar
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir''')

    opcion = get_option()

    if opcion == 1:
        first_number, second_number = get_number()
        resultado = suma(first_number, second_number)
        print (f"La suma de {first_number} y {second_number} es {resultado}")

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print()

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
        print()

               
    elif opcion == 2:
        first_number, second_number = get_number()
        resultado = resta(first_number, second_number)
        print (f"La resta de {first_number} y {second_number} es {resultado}")

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print()

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()
        
        
    elif opcion == 3:
        first_number,second_number = get_number()
        resultado = multiplicacion(first_number,second_number)
        print (f"La multiplicación de {first_number} y {second_number} es {resultado}")

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print()

        if opcion2 == "n":  
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 4:
        first_number,second_number = get_number()
        resultado = division(first_number, second_number)

        print(f"la division de {first_number} y {second_number} es {resultado}")

        opcion2 = input("Deseas elegir otra opcion? (y/n):  ").lower() .strip()
        print()

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 5:
        print("Saliendo del sistema")
        break
        
    else :
        print(WARNING + "Error: opcion invalida" + ENDC)
        print()
        

