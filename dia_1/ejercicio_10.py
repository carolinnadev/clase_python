from funciones_10 import get_user_contraseña
import time

HEADER = '\033[95m'
OKBLUE = '\033[38;2;255;193;7m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

usuario_definido = "caro123"
contraseña_definida = "caro123"
intentos = 0

while intentos < 3:
    usuario, contraseña = get_user_contraseña()

    if usuario == usuario_definido and contraseña == contraseña_definida:
        print("Acceso concedido")
        break
    else:
        intentos += 1
        print(WARNING + "Usuario o contraseña inválidos, inténtalo nuevamente" + ENDC)

        if intentos == 3:
            print(WARNING + "Demasiados intentos. Espera un minuto." + ENDC)
            time.sleep(60)
            for seconds in range(60, 0, -1):
                print(f"\rTiempo restante: {seconds} segundos ", end="", flush=True)  #ACTUALIZA EL CONTADOR EN LA MISMA LÍNEA Y MUESTRA CADA CAMBIO INMEDIATAMENTE.
                time.sleep(1)

            print(OKBLUE + "\nYa puedes intentarlo nuevamente." + ENDC)
            intentos = 0