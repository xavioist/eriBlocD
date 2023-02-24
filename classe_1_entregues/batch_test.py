import os
import pytest

"""
To run this script:

pytest --no-header -v batch_test.py

and the student's grade is the number of tests they've passed out of 10

"""


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata_ex1 = [
    ([1, 2, 3, 4, 5], 15),
    ([1, 1, 1, 1, 1], 5),
    ([0, 0, 0, 4, 1, 1, 6], 12),
    ([0, 0, 0, 0], 0),
]

testdata_ex2 = [
    ("aqewirotuy", "qwrty"),
    ("AjEeOokkLkwa", "jkkLkw"),
    ("1sdfWWQ0 OiLkd636 Eddw", "1sdfWWQ0 Lkd636 ddw"),
]

testdata_ex3 = [
    ({"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5}, 6.5),
    ({"Alumne": "Ivan", "NIU": 1329908, "Nota_1": 0, "Nota_2": 0}, 0)
]

testdata_ex4 = [
    (
        {"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5},
        {"Alumne": "Paula", "NIU": 1429902, "Nota_1": 8.5, "Nota_2": 8.5},
        {"Alumne": "Genis", "NIU": 1326302, "Nota_1": 5, "Nota_2": 4},
        "Paula",
    )
]


######EX1###################################################################
"""paste here the student's function (don't forget the imports)
"""


def suma(x):
    if x == []:
        return 0
    return x.pop() + suma(x)


######EX2###################################################################
"""paste here the student's function (don't forget the imports)
"""


def remove_vocals(x):
    forbidden_letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    res = ""
    for elem in x:
        if elem not in forbidden_letters:
            res = res + elem
    return res


######EX3###################################################################
"""paste here the student's function (don't forget the imports)
"""


def calc_mitja(dict):
    return (dict["Nota_1"] + dict["Nota_2"]) / 2


######EX4###################################################################
"""paste here the student's function (don't forget the imports)
"""


def top_student(dic1, dic2, dic3):
    hof = []
    init_val = 0
    list_of_dics = [dic1, dic2, dic3]
    for dic in list_of_dics:
        nota = (dic["Nota_1"] + dic["Nota_2"]) / 2
        if nota >= init_val:
            hof = [dic["Alumne"]]
            init_val = nota
    return hof[0]


@pytest.mark.parametrize("test_X, result", testdata_ex1)
def test_func1(test_X, result):
    assert pytest.approx(suma(test_X), 0.000001) == result


@pytest.mark.parametrize("test_X, result", testdata_ex2)
def test_func2(test_X, result):
    assert remove_vocals(test_X) == result


@pytest.mark.parametrize("test_X, result", testdata_ex3)
def test_func3(test_X, result):
    assert calc_mitja(test_X) == result


@pytest.mark.parametrize("test_X, test_Y, test_Z, result", testdata_ex4)
def test_func4(test_X, test_Y, test_Z, result):
    assert top_student(test_X, test_Y, test_Z) == result


    