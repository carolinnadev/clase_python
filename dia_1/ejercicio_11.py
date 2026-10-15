
from funciones_11 import get_temperatura

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

temperatura,numero = get_temperatura()

if temperatura == "C":
    if numero < 10:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra frio")
    elif numero == 10 and numero < 25:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra templado")
    elif numero == 25 and numero < 35:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra caluroso")
    else:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra muy caluroso")

elif temperatura == "F":
    if numero < 10:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra frio")
    elif numero == 10 and numero < 25:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra templado")
    elif numero == 25 and numero < 35:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra caluroso")
    else:
        print(f"La temperatura ingresada es {numero}{temperatura}, el clima se encuentra muy caluroso")
else:
    print(WARNING + "Ingrese una temperatura valida" + ENDC)