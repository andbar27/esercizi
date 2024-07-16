from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass


class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        self.chiave = chiave

    @staticmethod
    def sposta_carattere(c: str, n: int) -> str:
        return chr(ord(c) + n)
    
    def codifica(self, testoInChiaro: str) -> str:
        testoCodificato = ""

        for c in testoInChiaro:
            testoCodificato += self.sposta_carattere(c, self.chiave)

        return testoCodificato
    
    def decodifica(self, testoCodificato: str):
        testoInChiaro = ""

        for c in testoCodificato:
            testoInChiaro += self.sposta_carattere(c, -self.chiave)

        return testoInChiaro
    


class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int) -> None:
        self.n = n

    
    @staticmethod
    def combinazione(testoInChiaro: str) -> str:
        lenght = len(testoInChiaro)
        half_len = lenght // 2
        even = lenght % 2
        if even:  half_len += 1

        first_half = testoInChiaro[:half_len]
        second_half = testoInChiaro[half_len:]

        testoCodificato = ""
        for i in range(lenght // 2):
            testoCodificato += first_half[i] + second_half[i]

        if even: 
            testoCodificato += first_half[-1]

        return testoCodificato


    @staticmethod
    def decombinazione(testoCifrato: str) -> str:
        lenght = len(testoCifrato)
        
        first_half = ""
        second_half = ""
        for i in range(lenght):

            if i % 2:   #even
                second_half += testoCifrato[i]
            
            else:
                first_half += testoCifrato[i]

        return first_half + second_half


    def codifica(self, testoInChiaro: str) -> str:

        for i in range(self.n):
            testoInChiaro = self.combinazione(testoInChiaro)

        return testoInChiaro
    


    def decodifica(self, testoCodificato: str) -> str:

        for i in range(self.n):
            testoCodificato = self.decombinazione(testoCodificato)

        return testoCodificato

    


with open("test.txt", "r") as f:
    testoInChiaro = f.readline()
    result = f.readline()


c = CifratoreAScorrimento(3)

t = c.codifica(testoInChiaro)
print(t)
print(result)

r = c.decodifica(t)
print(r)

with open("output.txt", "w") as f:
    f.write(t)
    f.write(r)

cc = CifratoreACombinazione(5)

t = cc.codifica(testoInChiaro)
r = cc.decodifica(t)

with open("output.txt", "a") as f:
    f.write(t)
    f.write(r)

print(t, "\n",r)