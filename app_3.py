"""
Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:
"""

if __name__ == "__main__":

    print("<< Sumando números impares >>")

    result = 0
    for num in range(0, 100):
        if num % 2 != 0:
            result += num
            print(f"Número impar: {num}")

    print(f"Total: {result}")

    print(f"Total: {sum(range(1, 100, 2))}")
