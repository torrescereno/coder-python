"""
Escribe un programa que pida al usuario cuantos números quiere introducir.
Luego lee todos los números y realiza una media aritmética

"""
from utilities import check_system, clear_console

if __name__ == "__main__":

    command = check_system()
    list_numbers = []
    max_number = 0

    while True:
        try:
            max_number = int(
                input("Ingresa la cantidad de números que deseas calcular: ")
            )
            for x in range(0, max_number):
                value = int(input(f"Ingresa el valor del numero {x+1}: "))
                list_numbers.append(value)
            print(f"El promedio es: {sum(list_numbers) / max_number}")
            break
        except Exception:
            clear_console(command)
            print("Valor erroneo. Por favor ingrese un número")
