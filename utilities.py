import os
import platform


def check_system():
    system_operation = platform.system()
    command = "clear"
    if (
        system_operation == "win32"
        or system_operation == "cygwin"
        or system_operation == "Windows"
    ):
        command = "cls"
    return command


def clear_console(command):
    return os.system(command)


def print_menu(menu_options):
    for key in menu_options.keys():
        print(f"{key} -- {menu_options[key]}")
