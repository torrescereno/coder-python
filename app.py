a = 10
b = -5
c = "Hola"
d = [1,2,3]
e = (4,5,6)

# ====================================

numero_1 = int(input("Ingresa la primera nota: "))
numero_2 = int(input("ingresa la segunda nota: "))
numero_3 = int(input("ingresa la tercera nota: "))

media = (numero_1*15/100) + (numero_2*35/100) + (numero_3*50/100)
print("La nota media es", media)

# ====================================

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

for i, val in enumerate(matriz):
    matriz[i].append(sum(val))

print(matriz)
