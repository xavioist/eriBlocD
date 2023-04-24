"""Ex_0.2

Fes una funció check(numero) que, donat qualsevol nombre enter positiu,
digui si és parell i divisible per 7. Si no ho és, que imprimeixi per pantalla si és
parell, divisible per 7 o cap de les opcions anteriors.

Fes una altra funció resta(numero) que et digui quants cops se li pot restar 3 abans de que el nombre
esdevingui negatiu.
"""

i = 8


def check(i):
    if i % 2 == 0 and i % 7 == 0:
        print(i, " es parell i divisible entre 7")
        return True
    elif i % 2 == 0:
        print(i, "es parell, pero no divisible entre 7")
        return True
    elif i % 7 == 0:
        print(i, "es divisible entre 7, pero no parell")
        return True
    print(i, "ni es parell, ni es divisible per 7")
    return False


def resta(i):
    counter = 0
    while i > 0:
        counter += 1
        i -= 3

    print("pot fer-ho ", counter, " vegades")


check(i)
resta(i)
