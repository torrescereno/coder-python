"""
Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio
"""

from utilities import check_system, clear_console


def intermedio(a, b):
    return (a + b) / 2


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            print("Calculo del número intermedio")
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            result = intermedio(a, b)
            print(f"El punto intermedio es: {result}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar un número")
