import os
import pytest

"""Test ex_04: Fes un diccionari (dict_alumne) per la fitxa d'un alumne i les notes dels dos últims parcials.
Fes una funció que rebi d'input el diccionari i retorni la mitjana de les notes dels últims dos parcials.

    Returns:
        {"Alumne" : "Joanet", "NIU" : 1329902, "Nota 1": 8.5, "Nota 2" : 4.5} -> 6.5
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [({"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5}, 6.5)]

dic = {"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5}


def calc_mitja(dict):
    return (dict["Nota_1"] + dict["Nota_2"]) / 2


###INSERT STUDENT FUNCTION HERE


##############################


@pytest.mark.parametrize("test_X, result", testdata)
def test_func(test_X, result):
    assert calc_mitja(test_X) == result
