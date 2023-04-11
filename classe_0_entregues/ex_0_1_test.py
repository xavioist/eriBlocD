"""Ex 0.1
Defineix dues variables:

var1 = "66"

var2 = "foo bar baz"


Fes una funció generator(var1, var2) que, donades var1 i var2, sigui capaç de generar var3

var3 = ["66", "foo bar baz", "bar"]

PISTA: Pots fer servir mètode append() de les llistes i el slicing de llistes de python: https://www.w3schools.com/python/python_strings_slicing.asp
"""

var1 = "66"

var2 = "foo bar baz"


def generator(var1, var2):
    out = []
    out.append(var1)
    out.append(var2)

    tmp = var2[3:7]
    out.append(tmp)
    return out


print(generator(var1, var2))
