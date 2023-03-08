"""Ex 0.1
Defineix dues variables:

var1 = 66

var2 = "foo bar baz"


Fes una funció generator(var1, var2) que, donades var1 i var2, sigui capaç de generar var3

var3 = [66, "foo", 132, "ar"]

PISTA: Pots fer servir el slicing de llistes i strings i el mètode append() de les llistes 
"""

var1 = 66

var2 = "foo bar baz"


def generator(var1, var2):
    out = []
    out.append(var1)
    out.append(var2[0:3])
    out.append(2 * var1)
    out.append(var2[5:7])
    return out


print(generator(var1, var2))
