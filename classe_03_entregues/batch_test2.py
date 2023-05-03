import os
import pytest

"""
To run this script:

pytest --no-header -v batch_test.py

and the student's grade is the number of tests they've passed out of 10

"""

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


testdata5 = [
    (
        {"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5},
        {"Alumne": "Paula", "NIU": "1429902", "Nota_1": 8.5, "Nota_2": 8.5},
        {"Alumne": "Genis", "NIU": 1326302, "Nota_1": 5, "Nota_2": 4},
        4086106,
    )
]
testdata6 = [
    ([1, 1, 2, 3, 3, 4, 5, 6, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
    (
        ["a", 3, 6, 88, 6, "p", "pa", 43, "", 44, 88],
        ["a", 3, 6, 88, "p", "pa", 43, "", 44],
    ),
]

testdata7 = [("hola amigo", 3, ["k", "r", "o", "d", "c", "d", "p", "l", "j", "r"])]

testdata7_1 = [("krodcdpljr", 3, ["h", "o", "l", "a", " ", "a", "m", "i", "g", "o"])]

testdata8 = [
    ("Pop goes the weasel", "Pop"),
    ("\tje je", "je"),
    (" trap ahead", "trap"),
    ('"estic chill"', "estic"),
    ("benvolgut, permet-me suposar", "benvolgut"),
]


######EX1###################################################################
"""paste here the student's function (don't forget the imports)
"""


def suma_nius(dic1, dic2, dic3):
    """suma_nius

    Args:
        dic1 (dict): diccionari amb les dades d'un alumne
        dic2 (dict): ídem
        dic3 (dict): ídem

    Returns:
        int: suma dels NIUs dels tres alumnes
    """
    niu_total = 0
    list_of_dics = [dic1, dic2, dic3]
    for dic in list_of_dics:
        """niu_total += dic[
            "NIU"
        ]"""  # NO TINDRAN EL CAST A INT (TypeError: unsupported operand type(s) for +=: 'int' and 'str')
        niu_total += int(dic["NIU"])
    return niu_total


######EX2###################################################################
"""paste here the student's function (don't forget the imports)
"""


def remove_dups(x):
    """remove_dups

    Args:
        x (list): llista d'elements

    Returns:
        list: retorna una llista sense elements repetits
    """
    elements_unics = []
    for element in x:
        if element not in elements_unics:
            elements_unics.append(element)
        else:
            pass
            # x.pop(element)

    return elements_unics
    # return x


######EX3###################################################################
"""paste here the student's function (don't forget the imports)
"""
import string

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


######EX4###################################################################
"""paste here the student's function (don't forget the imports)
"""


def first_word(x):
    res = ""
    forbidden = [
        "\n",
        "\t",
        "\b",
        ",",
        ";",
        '"',
        ".",
        " ",
        "-",
        "--",
        "^",
        "$",
        "%",
        "/",
        "\t\t",
    ]

    if x[0] in forbidden:
        x = x[1:]

    for word in x:
        if word not in forbidden:
            res = res + word
        elif word in forbidden:
            return res


@pytest.mark.parametrize("test_X, test_Y, test_Z, result", testdata5)
def test_func5(test_X, test_Y, test_Z, result):
    assert suma_nius(test_X, test_Y, test_Z) == result


@pytest.mark.parametrize("test_X, result", testdata6)
def test_func6(test_X, result):
    assert remove_dups(test_X) == result


@pytest.mark.parametrize("test_X, test_Y, result", testdata7)
def test_func7(test_X, test_Y, result):
    assert cypher(test_X, test_Y) == result


@pytest.mark.parametrize("test_X, test_Y, result", testdata7_1)
def test_func7_1(test_X, test_Y, result):
    assert decypher(test_X, test_Y) == result


@pytest.mark.parametrize("test_X, result", testdata8)
def test_func8(test_X, result):
    assert first_word(test_X) == result
