"""

Dadas dos listas,
debes generar una tercera con todos los elementos que se repitan en ellas,
pero no debe repetirse ningún elemento en la nueva lista:

Input

lista_1 = ["h",'o','l','a',' ', 'm','','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']


"""

import collections

if __name__ == "__main__":

    first_list = list(input("Agrega una frase que se convertira en la primera lista: "))
    second_list = list(input("Agrega una frase que se convertira en la segunda lista: "))

    result_list = []

    for item in first_list:
        if item in second_list and item not in result_list:
            result_list.append(item)
    print(result_list)

    ## ------------- ##

    result_list = first_list + second_list

    # Resultado con collections
    print([x for x, y in collections.Counter(result_list).items() if y > 1])
