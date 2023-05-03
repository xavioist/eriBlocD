import os
import pytest

"""Test ex_05: Arregla aquesta funció per a que faci el que se suposa que ha de fer.

    Returns: 
    suma_nius(dic1,dic2,dic3) -> 4086106
        
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [
    (
        {"Alumne": "Joanet", "NIU": 1329902, "Nota_1": 8.5, "Nota_2": 4.5},
        {"Alumne": "Paula", "NIU": "1429902", "Nota_1": 8.5, "Nota_2": 8.5},
        {"Alumne": "Genis", "NIU": 1326302, "Nota_1": 5, "Nota_2": 4},
        4086106,
    )
]

dic1 = {"Alumne": "Joanet", "NIU": 1331616, "Nota_1": 8.5, "Nota_2": 4.5}
dic2 = {"Alumne": "Paula", "NIU": 1429902, "Nota_1": 7, "Nota_2": 8.5}
dic3 = {"Alumne": "Genis", "NIU": 1526302, "Nota_1": 5, "Nota_2": 4}


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
        niu_total += dic[
            "NIU"
        ]  # NO TINDRAN EL CAST A INT (TypeError: unsupported operand type(s) for +=: 'int' and 'str')
        # niu_total += int(dic["NIU"])
    return niu_total


###INSERT STUDENT FUNCTION HERE


##############################


@pytest.mark.parametrize("test_X, test_Y, test_Z, result", testdata)
def test_func(test_X, test_Y, test_Z, result):
    assert suma_nius(test_X, test_Y, test_Z) == result
