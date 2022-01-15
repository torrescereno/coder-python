"""
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
Calcula el área de un círculo de 5 de radio
"""

import math

from utilities import check_system, clear_console


def area_circulo(r):
    return math.pi * (r * r)


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            print("Calculo del área de un círculo")
            r = float(input("Ingrese el radio: "))
            area = round(area_circulo(r), 2)
            print(f"El área del círculo es: {area}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar un número")
