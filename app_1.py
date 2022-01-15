"""
Realiza una función llamada area_rectangulo()
que devuelva el área del rectángulo a partir de una base y una altura.
Calcula el área de un rectángulo de 15 de base y 10 de altura
"""

from utilities import check_system, clear_console


def area_rectangulo(l, b):
    return l * b


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            print("Calculo del área de un rectángulo")
            l = int(input("Ingrese la altura "))
            b = int(input("Ingrese la base "))
            area = area_rectangulo(l, b)
            print(f"El area del rectangulo es: {area}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar un número")
