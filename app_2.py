"""

2) Escribe un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar,
debe repetirse el proceso hasta que lo introduzca correctamente.


"""

from utilities import check_system, clear_console

if __name__ == "__main__":
    command = check_system()
    print("Ingrese un valor impar")
    while True:
        try:
            value = int(input("Ingrese un numero: "))
            if value % 2 != 0:
                print("Se ingreso un valor impar")
                break
            print("Debes ingresar un valor impar :(")
        except Exception:
            clear_console(command)
            print("Valor erroneo. Por favor ingrese un numero")
