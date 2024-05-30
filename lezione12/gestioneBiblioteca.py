# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
#     Il libro deve essere inizialmente disponibile (non prestato).

class Libro:

    def __init__(self, title: str, author: str, loaned: bool = False) -> None:
        self.title = title
        self.author = author
        self.loanStatus = loaned

    def __str__(self) -> str:
        return self.title

    

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
class Biblioteca:

    def __init__(self) -> None:
        self.libri: list[Libro] = []


#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. 
#         Restituisce un messaggio di conferma.

    def aggiungi_libro(self, libro: Libro):

        if libro in self.libri:
            print("Libro già presente")
        
        else:
            self.libri.append(libro)


#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
#         Se non ci sono libri disponibili, restituisce un messaggio di errore.
    def mostra_libri_disponibili(self) -> list[str]:

        listaTitoli: list[str] = []

        listaTitoli = [str(libro) for libro in self.libri if isinstance(libro, Libro) and libro.loanStatus == False]
        # for libro in self.libri: 
        #     if isinstance(libro,Libro) and libro.loanStatus == False:
        #         listaTitoli.append(str(libro))

        if len(listaTitoli) == 0:
            print("libreria vuota")

        return listaTitoli


#     - presta_libro(titolo): Cerca un libro per titolo e, 
#         se disponibile e non già prestato, lo segna come disponibile. 
#         Restituisce un messaggio di stato.
    def presta_libro(self, titolo: str):

        for libro in self.libri:

            if(titolo == str(libro) and not libro.loanStatus):
                libro.loanStatus = True
                print(f"Tieni il libro {titolo}, è disponibile")

            else:
                print(f"Libro {titolo} già prestato")

#     - restituisci_libro(titolo): Cerca un libro per titolo e, 
#         se trovato e prestato, lo segna come disponibile. 
#         Restituisce un messaggio di stato.
    def restituisci_libro(self, titolo: str):

        for libro in self.libri:

            if(titolo == str(libro) and libro.loanStatus):
                libro.loanStatus = False
                print(f"Libro restituito: {titolo}")

            else:
                print(f"Libro {titolo} già prestato")

bbl = Biblioteca()
bbl.aggiungi_libro(Libro("ciao", "luca"))
bbl.aggiungi_libro(Libro("o1", "j"))
print(bbl.libri)
bbl.mostra_libri_disponibili()
bbl.presta_libro("ciao")
bbl.mostra_libri_disponibili()
bbl.restituisci_libro("ciao")
print("lista: ",bbl.libri)
print(bbl.mostra_libri_disponibili())
bbl.aggiungi_libro("bella")
print(bbl.mostra_libri_disponibili())