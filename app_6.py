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

# Números pares
print(list(range(0, 21, 2)))

# Números impares
print(list(range(-19, 0, 2)))

# Números múltiples de 5
print(list(range(0, 55, 5)))
