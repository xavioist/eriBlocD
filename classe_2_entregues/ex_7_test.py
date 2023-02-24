import os
import pytest
import string

"""Test ex_07 (difícil): Fes un programa que xifri un missatge (str) segons una clau (int) que tu li proporcionis.
El xifrat més simple d'aquest estil és el xifrat romà ( o xifrat Cèsar):
    
    https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
    
També has de poder fer el desxifrador. PISTA: fent "import string" i definint la variable 

    alphabet = list(string.ascii_lowercase)
    alphabet.append(" ")

Tenim una llista de totes les lletres de l'alfabet i de l'espai. Feu servir només lletres en minúscula i espais,
sense accents ni signes de puntuació. 
    Returns:
    
    cyph("hola amigo", 3) -> ["k", "r", "o", "d", "c", "d", "p", "l", "j", "r"] 
    decyph ("krodcdpljr", 3) -> ["h", "o", "l", "a", " ", "a", "m", "i", "g", "o"]
        
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [("hola amigo", 3, ["k", "r", "o", "d", "c", "d", "p", "l", "j", "r"])]

testdata2 = [("krodcdpljr", 3, ["h", "o", "l", "a", " ", "a", "m", "i", "g", "o"])]


alphabet = list(string.ascii_lowercase)
alphabet.append(" ")


def cypher(missatge, clau):
    cyph = []
    for m in missatge:
        if m in alphabet:
            increment = alphabet.index(m)
            m = alphabet[(clau + increment) % 27]
            cyph.append(m)

    return cyph


def decypher(missatge, clau):
    decyph = []
    for m in missatge:
        if m in alphabet:
            increment = alphabet.index(m)
            m = alphabet[(increment - clau) % 27]
            decyph.append(m)

    return decyph


@pytest.mark.parametrize("test_X, test_Y, result", testdata)
def test_func(test_X, test_Y, result):
    assert cypher(test_X, test_Y) == result


@pytest.mark.parametrize("test_X, test_Y, result", testdata2)
def test_func2(test_X, test_Y, result):
    assert decypher(test_X, test_Y) == result


"""res = cypher("hola amigo", 3)

print((res))

new_res = decypher(res, 3)

print(funcions.foldr_str(new_res))"""

###INSERT STUDENT FUNCTION HERE


##############################
