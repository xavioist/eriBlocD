import os
import pytest

"""Test ex_01: Fes una funció suma(x) que sumi tots els elements d'una llista ***sense fer servir loops for***
ni funcions que no estiguin al paquet estàndard de python (exceptuant la funció sum()).

    https://cs.famaf.unc.edu.ar/~hoffmann/pd18/martes23.html

    Returns:
        func([1,2,3]) -> 6
        
        
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [([1, 2, 3, 4, 5], 15), ([1, 1, 1, 1, 1], 5), ([0, 0, 0, 4, 1, 1, 6], 12)]


# Reference function:


###INSERT STUDENT FUNCTION HERE


def g1(x):
    if x == []:
        return 0
    return x.pop() + g1(x)


##############################


@pytest.mark.parametrize("test_X, result", testdata)
def test_func(test_X, result):
    assert pytest.approx(g1(test_X), 0.000001) == result
