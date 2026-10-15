from funciones_01 import get_name, edad

nombre = get_name()
Edad = edad()

if Edad >= 18 :
    print (f"{nombre} tienes {Edad} eres mayor de edad")
else:
    print(f"{nombre} tienes {Edad} aun eres menor de edad")


