from funciones_12 import get_side, get_sides, classify_triangle

HEADER = '\033[38;2;0;200;255m'
OKBLUE = '\033[38;2;80;140;255m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[38;2;255;0;0m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


first_side, second_side, third_side = get_sides()
result = classify_triangle(first_side, second_side, third_side)

print(HEADER + "=" * 50 + ENDC)
print(f"Los lados son: {first_side}, {second_side}, {third_side}")
print(f"El triángulo es: {result}")
print(HEADER + "=" * 50 + ENDC)