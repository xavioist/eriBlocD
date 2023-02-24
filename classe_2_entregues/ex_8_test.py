import os
import pytest

"""Test ex_03: Fes una funció first_word(x) que retorni la primera paraula d'una frase.

    Returns:
        "hola, bon dia" -> "hola"
    """


TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

testdata = [
    ("Pop goes the weasel", "Pop"),
    ("\tje je", "je"),
    (" trap ahead", "trap"),
    ('"estic chill"', "estic"),
    ("benvolgut, permet-me suposar", "benvolgut"),
]


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


###INSERT STUDENT FUNCTION HERE


##############################


@pytest.mark.parametrize("test_X, result", testdata)
def test_func(test_X, result):
    assert first_word(test_X) == result
