# Scrivi un programma in Python che gestisca un magazzino. 
# Il programma deve permettere di aggiungere prodotti al magazzino, 
# cercare prodotti per nome e verificare la disponibilità di un prodotto.


# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)

class Prodotto:

    def __init__(self, nome: str, quantita: int) -> None:
        self.nome = nome
        self.quantita = quantita

    def __str__(self) -> str:
        return self.nome
        
 
# Definisci una classe Magazzino:

class Magazzino:

    def __init__(self) -> None:
        self.prodotti = []


# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
    def cerca_prodotto(self, nome: str) -> Prodotto:
        
        myProdotto: Prodotto = None
        for prodotto in self.prodotti:
            if nome == str(prodotto):
                myProdotto = prodotto

        return myProdotto


# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.

    def aggiungi_prodotto(self, prodotto: Prodotto):
        
        myProdotto = self.cerca_prodotto(prodotto.nome)

        if myProdotto:  # Se il prodotto è presente
            myProdotto.quantita += prodotto.quantita

        else:
            self.prodotti.append(prodotto)


# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

    def verifica_disponibilita(self, nome: str) -> str:

        if self.cerca_prodotto(nome):
            print(f"{nome} è disponibile")
            return True
        
        print(f"{nome} non è disponibile")
        return False
    

mgz1 = Magazzino()
mgz1.aggiungi_prodotto(Prodotto("oreo", 10))
mgz1.aggiungi_prodotto(Prodotto("cocacola", 11))
print(mgz1.cerca_prodotto("pepsi"))
print(mgz1.cerca_prodotto("oreo"))
mgz1.verifica_disponibilita("oreo")
mgz1.verifica_disponibilita("pepsi")
mgz1.verifica_disponibilita("cocacola")
