class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


persona_1 = Person("Carles", 23)
persona_2 = Person("Sílvia", 24)

print(persona_1.name)

persona_1.name = "Mohammed"

print(persona_1.name)
