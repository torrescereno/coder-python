"""
1)  Escribe un programa que lea dos números por teclado y
    permita elegir entre 4 opciones en un menú:


* Mostrar una suma de los dos números
* Mostrar una resta de los dos números (el primero menos el segundo)
* Mostrar una multiplicación de los dos números
* Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
* En caso de no introducir una opción válida, el programa informará de que no es correcta.

"""


import requests

from utilities import clear_console, check_system, print_menu

menu_options = {
    1: "Sumar dos numeros",
    2: "Restar dos numeros",
    3: "Multiplicar dos numeros",
    4: "Quotes 🎈",
    5: "Salir",
}

URL = "https://zenquotes.io/api/random"


def get_values():
    value_1 = int(input("Ingrese primer valor: "))
    value_2 = int(input("Ingrese segundo valor: "))
    return value_1, value_2


if __name__ == "__main__":
    command = check_system()
    while True:
        print_menu(menu_options)
        option = ""
        try:
            option = int(input("Por favor seleccione una opcion: "))

            if option in (1, 2, 3):
                value_1, value_2 = get_values()

            if option == 1:
                clear_console(command)
                print(
                    f"""
                Valores ingresados: {value_1} {value_2}
                La suma de los valores es: {value_1 + value_2}
                """
                )

            elif option == 2:
                clear_console(command)
                print(
                    f"""
                Valores ingresados: {value_1} {value_2}
                La resta de los valores es: {value_1 - value_2}
                """
                )

            elif option == 3:
                clear_console(command)
                print(
                    f"""
                Valores ingresados: {value_1} {value_2}
                La multiplicacion de los valores es: {value_1 * value_2}
                """
                )

            elif option == 4:
                clear_console(command)
                r = requests.get(URL, "GET")
                response = r.json()

                print(
                    f"""
                "{response[0]['q']}"
                Autor: {response[0]['a']}
                    """
                )

            elif option == 5:
                clear_console(command)
                print("Gracias por usar el programa")
                break
            else:
                raise

        except Exception:
            clear_console(command)
            print("Valor erroneo. Por favor ingrese un numero")
