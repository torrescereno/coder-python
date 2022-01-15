"""
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
La primera con los números pares, y la segunda con los números impares:
"""
from utilities import check_system, clear_console


def separar(a):
    par = []
    imp = []
    for num in a:
        par.append(num) if num % 2 == 0 else imp.append(num)
    par.sort()
    imp.sort()
    return par, imp


if __name__ == "__main__":
    command = check_system()
    try:
        while True:
            a = []
            print("Obtener pares e impares")
            n = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))
            for i in range(0, n):
                ele = int(input("Ingrese un número: "))
                a.append(ele)
            par, imp = separar(a)
            print(f"Lista de números pares: {par}")
            print(f"Lista de números impares: {imp}")
            break
    except Exception:
        clear_console(command)
        print("Debe ingresar una lista")
