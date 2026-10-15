HEADER = '\033[38;2;0;200;255m'
OKBLUE = '\033[38;2;80;140;255m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def get_side(side_name):
    while True:
        try:
            side = float(input(f"Ingrese el lado {side_name} del triángulo: "))

            if side > 0:
                return side
            else:
                print(WARNING + "El lado debe ser mayor que 0." + ENDC)

        except ValueError:
            print(WARNING + "Debes ingresar un número válido." + ENDC)


def get_sides():
    while True:
        first_side = get_side("1")
        second_side = get_side("2")
        third_side = get_side("3")

        if first_side + second_side > third_side and first_side + third_side > second_side and second_side + third_side > first_side:
            return first_side, second_side, third_side
        else:
            print(WARNING + "Los lados ingresados no forman un triángulo válido. Inténtalo nuevamente." + ENDC)


def classify_triangle(first_side, second_side, third_side):
    if first_side == second_side and second_side == third_side:
        return "Equilátero"
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        return "Isósceles"
    else:
        return "Escaleno"