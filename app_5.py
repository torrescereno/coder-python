"""

Escribe un programa que pida al usuario un número entero del 0 al 9,
y que mientras el número no sea correcto se repita el proceso.
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

"""

if __name__ == "__main__":
    list_numbers = []
    while True:
        try:
            number = int(input("Ingresa un numero entre 0 a 9: "))
            if number < 10 and number >= 0:
                list_numbers.append(number)
            else:
                break
        except Exception:
            break

    print(f"Lista de numeros {list_numbers}")