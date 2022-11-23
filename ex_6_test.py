import os
import pytest

"""Test ex_06: Arregla aquesta funció per a que faci el que se suposa que ha de fer.

    Returns: llista amb duplicats -> elimina els duplicats de la llista
        
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [
    ([1, 1, 2, 3, 3, 4, 5, 6, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
    (
        ["a", 3, 6, 88, 6, "p", "pa", 43, "", 44, 88],
        ["a", 3, 6, 88, "p", "pa", 43, "", 44],
    ),
]


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
            # pass
            x.pop(element)

    # return elements_unics
    return x


###INSERT STUDENT FUNCTION HERE


##############################


@pytest.mark.parametrize("test_X, result", testdata)
def test_func(test_X, result):
    assert remove_dups(test_X) == result
