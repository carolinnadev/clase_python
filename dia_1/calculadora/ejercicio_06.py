# importo las funciones que voy a usar
from dia_1.calculadora.funciones_06 import get_option, get_number, get_numbers, get_number_division, get_number_potencia, get_number_raiz_cuadrada, suma, resta, multiplicacion, division, potencia, raiz_cuadrada, raiz_cubica

#aplico el color que quiero usar en los errores
HEADER = '\033[38;2;0;200;255m'
OKBLUE = '\033[38;2;80;140;255m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Muestro el menu y pido la opcion que desee realizar
while True :

    print (OKBLUE + '''Elige la operacion que vas a realizar
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Potencia
        6. Raiz cadrada
        7. Raiz cubica
        8. Salir''' + ENDC)

    opcion = get_option()
    print(HEADER + "="*50 + ENDC) #FORMA DE INGRESAR EL COLOR

    if opcion == 1:
        first_number, second_number = get_numbers()
        resultado = suma(first_number, second_number)
        print (f"La suma de {first_number} y {second_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
        print()

               
    elif opcion == 2:
        first_number, second_number = get_numbers()
        resultado = resta(first_number, second_number)
        print (f"La resta de {first_number} y {second_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()
        
        
    elif opcion == 3:
        first_number,second_number = get_numbers()
        resultado = multiplicacion(first_number,second_number)
        print (f"La multiplicación de {first_number} y {second_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n): ").lower().strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":  
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 4:
        first_number,second_number = get_number_division()
        resultado = division(first_number, second_number)

        print(f"la division de {first_number} y {second_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n):  ").lower() .strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 5:
        first_number,second_number = get_number_potencia()
        resultado = potencia(first_number, second_number)

        print(f"la potencia de {first_number} y {second_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n):  ").lower() .strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 6:
        first_number= get_number_raiz_cuadrada()
        resultado = raiz_cuadrada(first_number)

        print(f"la raiz cuadrada de {first_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n):  ").lower() .strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()

    elif opcion == 7:
        first_number = get_number()
        resultado = raiz_cubica(first_number)

        print(f"la raiz cubica de {first_number} es {resultado}")
        print(HEADER + "="*50 + ENDC)

        opcion2 = input("Deseas elegir otra opcion? (y/n):  ").lower() .strip()
        print(HEADER + "="*50 + ENDC)

        if opcion2 == "n":
            print("Sistema finalizado")
            break
        elif opcion2 != "y":
            print(WARNING + "Error: ingresa 'y' o 'n'." + ENDC)
            print()                        

    elif opcion == 8:
        print("Saliendo del sistema")
        break
        
    else :
        print(WARNING + "Error: opcion invalida" + ENDC)
        print()
        