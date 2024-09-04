import unittest
from src.Persona import Persona
from src.Paziente import Paziente
from src.Dottore import Dottore
from src.Fattura import Fattura

class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.persona: Persona = Persona("Andrea", "Barbato")


    def test_initPersona(self):
        self.assertEqual(self.persona.first_name, "Andrea", "Errore initPersona, first_name")
        self.assertEqual(self.persona.last_name, "Barbato", "Errore initPersona, second_name")


    def test_setName(self):
        self.persona.setName("Andrew")
        self.assertEqual(self.persona.getName(), "Andrew", "Errore test_setName")


    def test_setLastName(self):
        self.persona.setLastName("Berbatov")
        self.assertEqual(self.persona.getLastname(), "Berbatov", "Errore test_setLastName")


    def test_setAge(self):
        self.persona.setAge(27)
        self.assertEqual(self.persona.getAge(), 27, "Errore test_setAge")

    
class TestDottore(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.dottore: Dottore = Dottore("Gino", "Strada", "Ginecologia", 80.00)
        self.dottore.setAge(31)


    def test_initDoctor(self):
        self.assertEqual(self.dottore.specialization, "Ginecologia", "Errore test_initDoctor, specialization")
        self.assertEqual(self.dottore.parcel, 80, "Errore test_initDoctor, parcel")
    

    def test_isValidDoctor(self):
        self.assertEqual(self.dottore.isAValidDoctor(), True, "Errore test_isAValidDoctor")
        self.dottore.setAge(30)
        self.assertEqual(self.dottore.isAValidDoctor(), False, "Errore test_isAValidDoctor")
        self.dottore.setAge(33)


class TestPaziente(unittest.TestCase):
    
    def setUp(self) -> None:
        self.pazienti = Paziente("Flaminia", "Pette", "03")


    def test_initPaziente(self):
        self.assertEqual(self.pazienti.getidCode(), "03", "Errore test_initPaziente")



class TestFattura(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.persona: Persona = Persona("Andrea", "Barbato")

        self.dottore: Dottore = Dottore("Gino", "Strada", "Ginecologia", 80.00)
        self.dottore.setAge(33)

        self.pazienti: list[Paziente] = []
        self.pazienti.append(Paziente("Luca", "Dido", "01"))
        self.pazienti.append(Paziente("Andrea", "Bardi", "02"))
        self.pazienti.append(Paziente("Flaminia", "Pette", "03"))

        self.fattura = Fattura(self.pazienti, self.dottore)

    
    def test_initFattura(self):
        self.assertEqual(self.fattura.salary, 0, "Errore test_initFattura")


    def test_getSalary(self):
        self.assertEqual(self.fattura.getFatture(), len(self.fattura.patient), "Errore test_getSalary, numero fatture")
        self.assertEqual(self.fattura.getSalary(), 80*len(self.fattura.patient), "Errore test_getSalary, valore salario")


    def test_AddRemovePatient(self):
        self.fattura.addPatient(Paziente("a","b","04"))
        self.assertEqual(len(self.fattura.patient), 4, "Errore test_addPatient")

        self.fattura.removePatient("04")
        self.assertEqual(len(self.fattura.patient), 3, "Errore test_removePatient")

    









if __name__ == "__main__": 
    unittest.TestCase()