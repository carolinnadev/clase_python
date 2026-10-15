
from funciones_08 import get_number

grade = get_number()

if grade < 70:
    print(f"tu nota es {grade} has reprobado")
elif grade >= 70 and grade <= 79:
    print(f"tu nota es {grade} promedio, has aprobado")
elif grade >= 80 and grade <=89:
    print(f"tu nota es {grade} buena, has aprobado")
elif grade >= 90 and grade <=100:
    print(f"tu nota es {grade} excelente, has aprobado")
else:
    print("Enter a valid grade")