"""Ex 0.3

Fes una funció func(num1, num2) que, donats dos nombres enters positius,
retorni el seu producte si aquest és més gran que 100 i que si no, retorni
la seva suma
"""


def func(num1, num2):
    if num1 * num2 > 100:
        return num1 * num2
    else:
        return num1 + num2
