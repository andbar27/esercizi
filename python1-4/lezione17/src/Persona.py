class Persona:

    def __init__(self, first_name: str, last_name: str) -> None:

        flagValueError = True
        if not isinstance(first_name, str):
            self.first_name = None
            self.age = None
            flagValueError = False
            print("Il nome inserito non è una stringa!")
        if not isinstance(last_name, str):
            self.last_name = None
            self.age = None
            flagValueError = False
            print("Il cognome inserito non è una stringa!")

        if flagValueError:
            self.first_name = first_name
            self.last_name = last_name
            self.age = 0


    def setName(self, first_name: str):
        
        if not isinstance(first_name, str):
            print("Il nome inserito non è una stringa!")
        
        else:
            self.first_name = first_name


    def setLastName(self, last_name: str):
        
        if not isinstance(last_name, str):
            print("Il cognome inserito non è una stringa!")
        
        else:
            self.last_name = last_name


    def setAge(self, age: int):
        
        if not isinstance(age, int):
            print("L'età deve essere un numero intero!")
        
        else:
            self.age = age

    
    def getName(self):
        return self.first_name
    

    def getLastname(self):
        return self.last_name
    

    def getAge(self):
        return self.age
    

    def greet(self):
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni!")

    

    