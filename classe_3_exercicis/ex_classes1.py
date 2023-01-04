"""Exemple de classes
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name


class Student(Person):
    def __init__(self, name, age, niu, grade_list):
        super().__init__(name, age)
        self.niu = niu
        self.grade_list = grade_list

    def average_grade(self):
        from functools import reduce

        sum = reduce(lambda a, b: a + b, self.grade_list)
        return sum / len(self.grade_list)


person_3 = Student("Kyle", 22, 1329983, [5, 6, 7])
person_3.change_name("Johnny")

print(person_3.average_grade())  # 6.0

persona_1 = Person("Carles", 23)
persona_2 = Person("Sílvia", 24)

persona_1.change_name("Mohammed")


def double(x):
    return x + x


lambda x: x + x
