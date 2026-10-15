# IMPORTAMOS LAS FUNCIONES
from funciones_01 import get_name, edad

#GUARDAMOS LOS DATOS EN VARIABLES
nombre = get_name()
Edad = edad()

#UTILIZAMOS IF PARA IDENTIFICAR LA EDAD
if Edad >= 18 :
    print (f"{nombre} tienes {Edad} eres mayor de edad")

else:
    print(f"{nombre} tienes {Edad} aun eres menor de edad")


