
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def get_name():
    while True:
        name = input("Ingrese su nombre: ").strip().lower()

        if name.isalpha():
            return name
        else:
            print(WARNING + "Error: Ingrese un nombre válido, solo letras." + ENDC)


def edad():
    while True:
        try:
            edad = int(input("Ingrese su edad:  "))
            return edad
        except ValueError:
            print(WARNING + "Error: Ingrese un numero valido" + ENDC)

    