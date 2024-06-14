from Persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)

        if not isinstance(idCode, str):
            self.idCode = None
        
        else:
            self.idCode = idCode

        
    def setIdCode(self, idCode):
        if isinstance(idCode, str):
            self.idCode = idCode


    def getidCode(self):
        return self.idCode
    

    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}")

        