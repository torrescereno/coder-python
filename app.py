"""
Generar una funcion que calcule el año bisiesto
"""

import os
import platform


def check_system():
    system_operation = platform.system()
    command = "clear"
    if (
        system_operation == "win32"
        or system_operation == "cygwin"
        or system_operation == "Windows"
    ):
        command = "cls"
    return command


def clear_console(command):
    return os.system(command)


def leap_year(year):
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    if is_leap_year:
        return f"El año {year} es bisiesto"

    return f"El año {year} no es bisiesto"


if __name__ == "__main__":
    command = check_system()
    while True:
        try:
            year = int(input("Ingrese un año: "))
            print(leap_year(year))
            break
        except Exception:
            clear_console(command)
            print("Valor erroneo. Por favor ingrese un numero")
