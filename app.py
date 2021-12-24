import os
import platform

menu_options = {
    1: 'Calcular notas',
    2: 'Salir'
}

def chaeck_system():
    system_operation = platform.system()
    command = 'clear'
    if system_operation == 'win32' or system_operation == 'cygwin':
        command = 'cls'
    return command

def clear_console(command): return os.system(command)

def print_menu():
    for key in menu_options.keys():
        print(f'{key} -- {menu_options[key]}')

if __name__=='__main__':
    command = chaeck_system()
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Por favor seleccione una opcion: '))

            if option == 1:
                value_1 = int(input('Ingrese primera nota: '))
                value_2 = int(input('Ingrese segunda nota: '))
                result = (value_1*40/100) + (value_2*60/100)
                clear_console(command)
                print(f"""
                Primera nota {value_1} correspondiente al 40%
                Segunda nota {value_2} correspondiente al 60%
                Resultado {result}
                """)
            elif option == 2:
                clear_console(command)
                print('Gracias por usar el programa')
                break
            else:
                raise
        except Exception:
            clear_console(command)
            print('Valor erroneo. Por favor ingrese un numero')

