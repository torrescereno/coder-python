"""

Escribe un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

"""

if __name__ == "__main__":
    list_numbers = [1, 3, 6, 9]
    while True:
        try:
            number = int(input("Ingresa un numero entre 0 a 9: "))
            if number in list_numbers:
                print(f"Ingresaste un número dentro de la lista: {list_numbers} 🥳")
            else:
                print("No ingresaste un número correcto 😔")
            break
        except Exception:
            print("Debes ingresar un número")