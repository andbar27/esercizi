from .Dottore import Dottore
from .Paziente import Paziente

class Fattura:


    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:

        if doctor.isAValidDoctor():
            self.fatture: int = len(patient)
            self.salary: int = 0
            self.patient: list[Paziente] = []
            if patient != None:
                self.patient = patient
            self.doctor: Dottore = doctor

        else:
            self.fatture = None
            self.salary = None
            self.patient = None
            self.doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    
    def getFatture(self):
        self.fatture = len(self.patient)
        return self.fatture
    

    def getSalary(self):
        self.salary = self.fatture * self.doctor.getParcel()
        return self.salary
    

    def addPatient(self, newPatient: Paziente):
        
        if (not isinstance(newPatient, Paziente)) or newPatient in self.patient:
            return
        
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()

        print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}")


    def removePatient(self, idCode):
        print("idCode: ",idCode)
        for paziente in self.patient:
            print("paziente: ",paziente.getidCode()) 
            if paziente.getidCode() == idCode:
                self.patient.remove(paziente)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {idCode}")

        


    
    