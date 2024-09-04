import unittest

from ..lezione26 import CifratoreAScorrimento, CifratoreACombinazione

class TestCifratoreScorrimento(unittest.TestCase):

    def setUp(self):
        self.cifratorescorrimento = CifratoreAScorrimento(3)
        self.cifratorecombinazione = CifratoreACombinazione(3)

    def test_codificaScorrimento(self):
        file_path = "test.txt"
        with open(file_path, "r") as f:
            testoInChiaro = f.readline()
            ret = f.readline()

        result = self.cifratorescorrimento.codifica(testoInChiaro)
        self.assertEqual(result, ret, "Errore in codifica di cifratore a scorrimento")

        with open("output.txt", "a") as f:
            f.write(result)