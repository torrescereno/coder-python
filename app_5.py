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
                if number in list_numbers:
                    print("El número ya se encuentra en la lista")
                else:
                    list_numbers.append(number)
        except Exception:
            if list_numbers:
                print(f"La lista de números es: {list_numbers}")
            print("Finaliza el proceso")
            break
