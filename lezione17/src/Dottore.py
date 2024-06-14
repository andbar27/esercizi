from Persona import Persona

class Dottore(Persona):
    
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)


        if not isinstance(specialization, str):            
            self.specialization = None
            print("La specializzazione inserita non è una Stringa!")

        else:
            self.specialization = specialization


        if not isinstance(parcel, float):
            self.parcel = None
            print("La parcella inserita non è un float!")

        else:
            self.parcel = parcel

        
    def setSpecialization(self, specialization: str):
        
        if not isinstance(specialization, str):            
            self.specialization = None
            print("La specializzazione inserita non è una Stringa!")

        else:
            self.specialization = specialization


    def setParcel(self, parcel: float):

        if not isinstance(parcel, float):
            self.parcel = None
            print("La parcella inserita non è un float!")

        else:
            self.parcel = parcel


    def getSpecialization(self):
        return self.specialization
    

    def getParcel(self):
        return self.parcel
    

    def isAValidDoctor(self):

        if self.age > 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
            return True

        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
            return False


    def greet(self):
        super().greet()
        print(f"Sono un medico {self.specialization}")

