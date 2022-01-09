"""
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

* Todos los números del 0 al 10 [0, 1, 2, ..., 10]
* Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
* Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
* Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
* Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
"""

# Positivos
print(list(range(0, 11)))

# Negativos
print(list(range(-10, 1)))

# Numeros pares
print(list(range(0, 21, 2)))

# Numeros impares
numbers = range(-20, 1)
list_numbers = [num for num in numbers if num % 2 != 0]
print(list_numbers)

# Numeros múltiples de 5
numbers = range(0, 51)
list_numbers = [num for num in numbers if num % 5 == 0]
print(list_numbers)
