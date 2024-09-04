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
        

# CLASSI ASTRATTE ------------------------------------

from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    

    @abstractmethod
    def verso(self):
        
        pass

# ----------------------------------------------------

    # FUNZIONI DI CLASSE ---------------------------------

    n_instances = 0

    @classmethod
    def get_instance(cls):
        return cls.n_instances
    
    # ----------------------------------------------------


    # FUNZIONI STATICHE ----------------------------------

    @staticmethod
    def anno_casuale():
        import random
        return random.randint(-7000, 2024)
    
    @staticmethod
    def funzione_statica(): 
        print("Hello world", AbcAnimal.anno_casuale())

    # ----------------------------------------------------


"""class Cavallo(AbcAnimal):

    def __init__(self, nome) -> None:
        super().__init__()
        self.nome

cavallo = Cavallo("cav")"""

"""DA ERRORE PERCHÉ NON ABBIAMO DEFINITO IL METODO ASTRATTO VERSO"""

class Cane(AbcAnimal):

    def __init__(self, nome) -> None:
        super().__init__()

    def verso(self):
        print("Bau")

cane = Cane("can")
cane.verso()

AbcAnimal.funzione_statica()