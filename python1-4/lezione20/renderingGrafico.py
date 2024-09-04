from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Rettangolo(Forma):

    def __init__(self, base, altezza) -> None:
        super().__init__()
        self.tipo: str = "Rettangolo"
        self.base: int = base
        self.altezza: int = altezza


    def getArea(self) -> int:
        print(f"L'area di questo {self.tipo} vale: {self.base * self.altezza}")
        return self.base * self.altezza
    

    def render(self) -> None:

        print(f"Ecco un {self.tipo} di base {self.base} e altezza {self.altezza}!")

        for i in range(self.altezza):

            for j in range(self.base):

                sep = " "
                if i == 0 or i == self.altezza -1 or j == 0 or j == self.base - 1:
                    sep = "*"

                print(f"{sep}", end=" ")

            print()
                    
    



class Quadrato(Rettangolo):
    
    def __init__(self, lato) -> None:
        super().__init__(lato, lato)
        self.tipo = "Quadrato"




class Triangolo(Forma):

    def __init__(self, lato) -> None:
        super().__init__()
        self.tipo: str = "Triangolo"
        self.base: int = lato
        self.altezza: int = lato


    def getArea(self):
        print(f"L'area di questo {self.tipo} vale: {self.base * self.altezza / 2}")
        return (self.base * self.altezza) / 2
    
    # DA FINIRE, TRIANGOLO CON LATI DIVERSI
    def render(self):
        
        print(f"Ecco un {self.tipo} di base {self.base} e altezza {self.altezza}!")

        base = self.base
        altezza = self.altezza
        base2 = self.base 
        if base < altezza:
            temp = altezza
            altezza = base
            base = temp
            base2 = base

        for i in range(altezza):
            res = base - base2 + 1
            for j in range(res):
                #print(f"sb: {base}  -  b: {base2}", end="   ")
                sep = " "
                if i == 0 or i == altezza - 1 or j == 0 or j == res - 1:
                    sep = "*"

                print(f"{sep}", end=" ")

            base2 -= 1
            print()


    # def render(self) -> None:

    #     print(f"Ecco un {self.tipo} di base {self.base} e altezza {self.altezza}!")
    #     base = self.base

    #     for i in range(self.altezza):

    #         for j in range(self.base - base + 1):

    #             sep = " "
    #             if i == 0 or i == self.altezza -1 or j == 0 or j == self.base - base:
    #                 sep = "*"

    #             print(f"{sep}", end=" ")
            
    #         base -= 1
    #         print()
                    
    

r = Rettangolo(32,82)
r.render()
r.getArea()

print()
q = Quadrato(64)
q.render()
q.getArea()

print()
t = Triangolo(3)
t.render()
t.getArea()