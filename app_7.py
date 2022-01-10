"""

Dadas dos listas,
debes generar una tercera con todos los elementos que se repitan en ellas,
pero no debe repetirse ningún elemento en la nueva lista:

Input

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']


"""

if __name__ == "__main__":

    first_list = list(input("Agrega una frase que se convertira en la primera lista: "))
    second_list = list(input("Agrega una frase que se convertira en la segunda lista: "))

    serie = set()

    for item in first_list:
        serie.add(item)

    for item in second_list:
        serie.add(item)


    print(list(serie))