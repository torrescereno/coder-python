"""
Realizá una función llamada recortar() que reciba tres parámetros.
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
La función tendrá que cumplir lo siguiente:

1. Devolver el límite inferior si el número es menor que éste
2. Devolver el límite superior si el número es mayor que éste.
3. Devolver el número sin cambios si no se supera ningún límite.
"""

from utilities import check_system, clear_console


def recortar(a, b, c):
    if a < b:
        return b
    if a > c:
        return c
    return a


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            print("Calculo de la función recortar")
            a = int(input("Ingrese el número a recortar: "))
            b = int(input("Ingrese el límite inferior: "))
            c = int(input("Ingrese el límite superior: "))
            result = recortar(a, b, c)
            print(f"El resultado es: {result}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar un número")
