class Animal:
    def __init__(self, species, age) -> None:
        self.species = species
        self.age = age

class Cat(Animal):
    def __init__(self, nome, species, age) -> None:
        super().__init__(species, age)
        self.nome = nome

class Rabbit(Animal):
    def __init__(self, species, age) -> None:
        super().__init__(species, age)

class Person(Animal):
    def __init__(self, nome, surname, cf, age, species = "Homo Sapiens") -> None:
        super().__init__(species, age)
        self.nome = nome
        self.surname = surname
        self.cf = cf

class Student(Person):
    def __init__(self, nome, surname, cf, matricula, species, age) -> None:
        super().__init__(nome, surname, cf, age, species)
        self.matricula = matricula
        