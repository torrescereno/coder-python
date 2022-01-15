"""
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

1. Si el primer número es mayor que el segundo, debe devolver 1.
2. Si el primer número es menor que el segundo, debe devolver -1.
3. Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
"""

from utilities import check_system, clear_console


def relacion(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            print("Calculo de relación de números")
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            result = relacion(a, b)
            print(f"El resultado es: {result}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar un número")
