import os
import pytest

"""Test ex_02: Fes una funció remove_vocals(x) que elimini totes les vocals d'una string.

    Returns:
        KLK MANIN -> KLK MNN
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [
    ("aqewirotuy", "qwrty"),
    ("AjEeOokkLkwa", "jkkLkw"),
    ("1sdfWWQ0 OiLkd636 Eddw", "1sdfWWQ0 Lkd636 ddw"),
]

def remove_vocals(x):
    forbidden_letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    res = ""
    for elem in x:
        if elem not in forbidden_letters:
            res = res + elem
    return res


###INSERT STUDENT FUNCTION HERE


##############################


@pytest.mark.parametrize("test_X, result", testdata)
def test_func(test_X, result):
    assert remove_vocals(test_X) == result
