"""Ex 0.1
Donades aquestes dues variables:

var1 = "66"

var2 = "foo bar baz"

Fes una funció generator(var1, var2) que sigui capaç de generar var3 només a partir de var1 i var2.
Mira la pista del final de l'enunciat i ajuda't dels mètodes descrits per a fer l'exercici.

var3 = ["66", "foo bar baz", "bar"]

Un altre exemple d'execució podria ser:

var1 = "hola"
var2 = "com vas pep"

donaria com a resultat: var3 = ["hola", "com vas pep", "vas"]

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
