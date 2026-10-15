from funciones_03 import get_number

Number = get_number()

if Number > 0:
    print(f"el numero {Number} es positivo")
elif Number < 0:
    print(f"el numero {Number} es negativo")
else:
    print(f"el numero {Number} es igual a 0")