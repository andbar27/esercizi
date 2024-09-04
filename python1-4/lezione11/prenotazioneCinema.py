# - Film: Rappresenta un film con titolo e durata.

class Film:

    def __init__(self, title: str, duration: int) -> None:
        self.title = title
        self.duration = duration
 


# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

class Sala:

    def __init__(self, nId: int, film: Film, max_seats: int, booked_seats: int = 0) -> None:
        self.nId = nId
        self.film = film
        self.max_seats = max_seats
        self.booked_seats = booked_seats


#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.

    def posti_disponibili(self) -> int:
        return self.max_seats - self.booked_seats


#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.

    def prenota_posti(self, num_posti: int) -> None:
        
        if num_posti <= self.posti_disponibili():
            self.booked_seats += num_posti
            print(f"Prenotazione di {num_posti} posti riuscita!")
        
        else:
            print(f"Prenotazione di {num_posti} non riuscita, posti non disponibili.")

    
    def __str__(self) -> str:
        return self.film.title

 
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.
class Cinema:

    def __init__(self) -> None:
        self.sale: list[Sala] = []


# - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.

    def aggiungi_sala(self, sala: Sala) -> None:

        if sala not in self.sale:
            self.sale.append(sala)


#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

    def prenota_film(self, titolo_film: str, num_posti: int):

        mySala: Sala = None
        for sala in self.sale:
            if titolo_film == str(sala):
                mySala = sala
        
        if mySala == None:
            print("Film non presente")

        mySala.prenota_posti(num_posti)


cine1 = Cinema()
sala1 = Sala(1, Film("C'è ancora domani", 120), 10)
cine1.aggiungi_sala(sala1)
cine1.prenota_film("C'è ancora domani", 11)
cine1.prenota_film("C'è ancora domani", 5)
cine1.prenota_film("C'è ancora domani", 6)
cine1.prenota_film("C'è ancora domani", 3)
cine1.prenota_film("C'è ancora domani", 5)
print(sala1.posti_disponibili())
