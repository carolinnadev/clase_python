from funciones_05 import get_number

first_number, second_numer = get_number()

if first_number > second_numer:
    print(f"el numero {first_number} es mayor que {second_numer}")
elif second_numer > first_number:
    print(f"el numero {second_numer} es mayor que {first_number}")
else:
    print(f"El numero {first_number} es igual a {second_numer}")