# colores son de https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

#  Se usa para aplicar color a errores como WARNING al inicio del print y ENDC al final del print concatenado

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def get_option():
    while True:
        try:
            opcion = int(input("Ingresa la opcion elegida "))
            return opcion
        except ValueError:
            print(WARNING + "Ingresa una opcion valida, debes ingresar una de las opciones anteriores" + ENDC)


def get_number():
    while True:
        try:
            first_number = int(input("Ingrese el primer numero "))
            return first_number
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)

def get_numbers():
    while True:
        try:
            first_number = int(input("Ingrese el primer numero "))
            second_number = int(input("Ingrese el segundo numero "))
            return first_number , second_number
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)

def get_number_division():
    while True:
        try:
            first_number = int(input("Ingrese el primer numero "))
            second_number = int(input("Ingrese el segundo numero "))
            while True: 
                if second_number == 0:
                    print (WARNING + "La divisiones no se pueden realizar entre 0 " + ENDC)
                    second_number = int(input("Por favor ingresa un numero diferente a 0:  "))
                else:
                    return first_number , second_number          
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)

def get_number_potencia():
    while True:
        try: 
            first_number = int(input("Ingrese el primer numero "))
            second_number = int(input("Ingrese el segundo numero "))
            while True:
                if first_number == 0 and second_number < 0:
                    print( WARNING + '''Ojo: En esta operación, si la base es 0, el exponente debe ser positivo.
                    Si la base es positiva, el exponente puede ser negativo.
                    De lo contrario, no podrás realizar la operación.
                    Vuelve a ingresar los números:''' + ENDC)
                    
                    first_number = int(input("Ingrese el primer numero "))
                    second_number = int(input("Ingrese el segundo numero "))
                else:
                    return first_number, second_number
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)
                    
def get_number_raiz_cuadrada():
    while True:
        try:
            first_number = int(input("Ingrese el primer numero "))
            while True: 
                if first_number < 0:
                    print (WARNING + "Esta operacion no se puede realizar entre un numero negativo " + ENDC)
                    first_number = int(input("Por favor ingresa un numero positivo:  "))
                else:
                    return first_number         
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)
        

def suma (a,b):
    return (a+b)

def resta (a,b):
    return (a-b)

def multiplicacion (a,b):
    return (a*b)

def division (a,b):
        return (a/b)

def potencia (a,b):
    return a ** b

def raiz_cuadrada (a):
    return a ** (1/2)

def raiz_cubica(a):
    if a < 0:
        return -((-a) ** (1 / 3))
    return a ** (1 / 3)

