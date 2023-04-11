"""Exemple de classes
"""


class Person:
    """Class Person

    atributs:
    name = (string)
    age = (int)

    mètodes:
       change_name(new_name)::str -> str::
            canvia el nom d'un objecte de la classe
            Person
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name


class Student(Person):
    """Classe Student, hereda name i age de la classe Person

    Un objecte de Student forma part de Person, però un objecte de Person
    no necessàriament és un Student.

    atributs:
    niu = (int)
    grade_list = (list[float])

    mètodes:
        average_grade():: Class_Student_object -> float::
            calcula la nota mitjana d'un Student i retorna un float
    """

    def __init__(self, name, age, niu, grade_list):
        # Aquesta línea ens dóna l'herència. Ara Student també té name i age
        super().__init__(name, age)
        self.niu = niu
        self.grade_list = grade_list

    def average_grade(self):
        # Prova a reescriure una funció que calculi la nota  mitjana d'un Student
        from functools import reduce

        sum = reduce(lambda a, b: a + b, self.grade_list)
        return sum / len(self.grade_list)


person_3 = Student("Kyle", 22, 1329983, [5, 6, 7])
person_3.change_name("Johnny")

print(person_3.average_grade())  # 6.0

persona_1 = Person("Carles", 23)
persona_2 = Person("Sílvia", 24)

persona_1.change_name("Mohammed")
