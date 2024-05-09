from typing import Tuple


class Person:

    def __init__(self,
                 name: str,
                 surname: str,
                 birth_date: str,
                 gender: str) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
    
    def age_calculator(self) -> int:
        return 2024 - int(self.birth_date[-4:])

person1: Person = Person("Andrea", "Barbato", "27/08/1996", "Male")
print(person1.age_calculator())

class Dependent(Person):
    def __init__(self, name: str, surname: str, birth_date: str, 
                 gender: str, working_time: int = 50) -> None:
        
        super().__init__(name, surname, birth_date, gender)
        self.working_time = working_time

    def fee_calculator(self) -> float:
        return 500.0

dependent1: Dependent = Dependent("Andrea", "Barbato", "27/08/1996", "Male")
print(dependent1.age_calculator())
print(dependent1.fee_calculator())
print(dependent1.working_time)

class Professor(Dependent):

    def __init__(self, name: str, surname: str, birth_date: str, 
                 gender: str, working_time: int = 50, subject: str = "") -> None:
        
        super().__init__(name, surname, birth_date, gender, working_time)
        self.subject = subject

prof1: Professor = Professor("Andrea", "Barbato", "27/08/1996", "Male", subject="Math")
print(prof1.age_calculator())
print(prof1.fee_calculator())
print(prof1.working_time)
print(prof1.subject)