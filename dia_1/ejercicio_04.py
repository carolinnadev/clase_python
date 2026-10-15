from funciones_03 import get_number

Number = get_number()
Residuo = Number%2

if Residuo == 0:
    print(f"el numero {Number} es par")
else:
    print(f"el numero {Number} es impar")
