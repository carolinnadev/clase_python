HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def get_temperatura():
    while True:
        try:
            temperatura = input("¿La temperatura está en Celsius (C) o Fahrenheit (F)?: ").strip().upper()

            if temperatura.isalpha() and temperatura in ["C", "F"]:
                numero = float(input("Ingrese la temperatura: "))
                return temperatura, numero
            else:
                print(WARNING + "Error: solo puede ingresar las letras C o F." + ENDC)

        except ValueError:
            print(WARNING + "Error: debe ingresar una temperatura numérica." + ENDC)