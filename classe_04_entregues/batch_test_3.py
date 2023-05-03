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

#### Insert student's function here
class Atom:
    def __init__(self, molec_weight, symbol, atomic_num, periodic, coords):
        self.molec_weight = molec_weight
        self.symbol = symbol
        self.atomic_num = atomic_num
        self.periodic = periodic
        self.coords = coords

    def compare_atoms(self, atom2):
        if self.molec_weight > atom2.molec_weight:
            print(self.symbol, " weights more")
        else:
            print(atom2.symbol, " weights more")

    def is_noble(self):
        if self.periodic == "Noble Gas":
            return True
        else:
            return False

    def distance(self, atom2):
        import numpy as np

        d = [(self.coords[i] - atom2.coords[i]) ** 2 for i in range(0, 3)]
        return np.sqrt(sum(d))

    def is_bond_possible(self, atom2, table):
        dist = self.distance(atom2)
        sym_1 = self.symbol
        sym_2 = atom2.symbol

        if (self.symbol or atom2.symbol) in "He Ne Ar Kr Xe Rn":
            print("Cannot form bond with noble gas!")
            return False

        for t in table:
            if sym_1 and sym_2 in t:
                if dist <= t[2]:
                    print(
                        "can be bonded, dist",
                        dist,
                        "is smaller than bond_dist = ",
                        t[2],
                    )
                    return True
                else:
                    print(
                        "cannot be bonded, dist",
                        dist,
                        "is greater than bond_dist = ",
                        t[2],
                    )
                    return False


table = [("C", "C", 1.54), ("C", "O", 1.43)]

carboni = Atom(12.011, "C", 12, "Non Metal", [2, 2, 0])
oxigen = Atom(15.999, "O", 16, "Non Metal", [1, 0, 1])

carboni.is_bond_possible(oxigen, table)


###################################


@pytest.mark.parametrize("test_X, result", testdata_ex1)
def test_func1(test_X, result):
    assert pytest.approx(suma(test_X), 0.000001) == result


@pytest.mark.parametrize("test_X, result", testdata_ex2)
def test_func2(test_X, result):
    assert remove_vocals(test_X) == result
