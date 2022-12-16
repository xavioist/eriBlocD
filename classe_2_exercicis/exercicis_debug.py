# Exercici 1

""" Arregla el programa per a que faci el que se suposa que ha de fer. Copia el programa en un full nou i arregla'l.
"""
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(weight, height):
    """Calcula el index de massa corporal d'un pacient

    Args:
        weight (int): el pes d'una persona
        height (float): l'alçada d'una persona

    Returns:
        bmi: índex de massa corporal, definit com pes/2*alçada
        PROBLEMA: Aparentment, sempre ens dona el mateix bmi per cada pacient...
    """
    return weight / (height ** 2)


for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is:", bmi)


# Exercici 2

""" Arregla el programa per a que faci el que se suposa que ha de fer. Copia el programa en un full nou i arregla'l.
"""


def minimum(mylist):
    """minimum: Retorna el nombre més petit d'una llista

    Args:
        mylist (list[int]): llista de nombres enters

    Returns:
        a: (int) Retorna el nombre més petit
        PROBLEMA: Aparentment, sempre retorna zero...
    """
    a = 0
    for x in range(1, len(mylist)):
        if mylist[x] < a:
            a = mylist[x]
    return a


print(minimum([1, 2, 3, 4, 5]))
