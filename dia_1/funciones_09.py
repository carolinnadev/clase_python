HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def get_price():
    while True:
        try:
            price = float(input("Ingrese el valor de su compra: "))
            while True: 
                if price < 0:
                    print (WARNING + "El valor de la compra no puede ser negativo" + ENDC)
                    calificacion = int(input("Por favor ingresa un valor valido:  "))
                else:
                    return price
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)