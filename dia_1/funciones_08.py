
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
            print("Las calificaciones van en un rango de 0 a 100")
            calificacion = int(input("Ingrese su calificacion: "))
            while True: 
                if calificacion < 0 or calificacion > 100:
                    print (WARNING + "Las calificaciones no pueden ser negativas o mayores a 100" + ENDC)
                    calificacion = int(input("Por favor ingresa una calificacion valida:  "))
                else:
                    return calificacion  
        except ValueError:
            print(WARNING + "Debes ingresar un número entero." + ENDC)