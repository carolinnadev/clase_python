HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def get_number():
    while True:
        try:
            first_number = int(input("Ingrese el numero "))
            return first_number
        
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)