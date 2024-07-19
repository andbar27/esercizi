from abc import ABC, abstractmethod

class Volo(ABC):

    def __init__(self, codiceVolo: str, nPosti: int) -> None:
        super().__init__()
        self.codiceVolo: str = codiceVolo
        self.nPosti: int = nPosti
        self.prenotazione: int = 0

    @abstractmethod
    def prenota_posto(self) -> None:
        pass

    @abstractmethod
    def posti_disponibili(self) -> None:
        pass


class VoloCommerciale(Volo):

    def __init__(self, codiceVolo: str, nPosti: int) -> None:
        super().__init__(codiceVolo, nPosti)
        self.posti_economica: int = int(nPosti * 0.7)
        self.posti_business: int = int(nPosti * 0.2)
        self.posti_prima: int = int(nPosti * 0.1)
        tot_posti = self.posti_economica + self.posti_business + self.posti_prima
        self.posti_economica += nPosti - tot_posti
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0
        

    def prenota_posto(self, posti: int, classe_servizio: str) -> None:

        def __prenota(disponibili, richista):
            diff = disponibili - richista
            if diff >= 0:
                return diff
            return -1


        if self.prenotazione == self.nPosti:
            print(f"Volo {self.codiceVolo} Completo!")
        


        if classe_servizio.lower() == "economica":
            res = __prenota(self.posti_economica - self.prenotazioni_economica, posti)

            if res != -1:
                self.prenotazioni_economica += posti 
                self.prenotazione += posti
                print(f"Riservati {posti} posti per il Volo {self.codiceVolo}")
            else:
                print(f"{posti} posti in economica non disponibili per Volo {self.codiceVolo}")



        elif classe_servizio.lower() == "business":
            res = __prenota(self.posti_business - self.prenotazioni_business, posti)

            if res != -1:
                self.prenotazioni_business += posti
                self.prenotazione += posti
                print(f"Riservati {posti} posti per il Volo {self.codiceVolo}")
            else:
                print(f"{posti} posti in business non disponibili per Volo {self.codiceVolo}")


        elif classe_servizio.lower() == "prima":
            res = __prenota(self.posti_prima - self.prenotazioni_prima, posti)

            if res != -1:
                self.prenotazioni_prima += posti
                self.prenotazione += posti
                print(f"Riservati {posti} posti per il Volo {self.codiceVolo}")
            else:
                print(f"{posti} posti in prima non disponibili per Volo {self.codiceVolo}")




    def posti_disponibili(self) -> None:
        posti_dict = dict()
        posti_dict["posti_disponibili"] = self.nPosti - self.prenotazione
        posti_dict["classe_economica"] = self.posti_economica - self.prenotazioni_economica
        posti_dict["classe_business"] = self.posti_business - self.prenotazioni_business
        posti_dict["classe_prima"] = self.posti_prima - self.prenotazioni_prima
        
        return posti_dict
    

    def __str__(self) -> str:
        return f"Volo Commerciale n° {self.codiceVolo}"



class VoloCharter(Volo):

    def __init__(self, codiceVolo: str, nPosti: int, prezzo: float) -> None:
        super().__init__(codiceVolo, nPosti)
        self.prezzo = prezzo

    
    def prenota_posto(self) -> None:
        if self.prenotazione == 0:
            self.prenotazione = self.nPosti
            print(f"Prenotazione eseguita con Successo, prezzo: {self.prezzo} - Volo {self.codiceVolo}")
        else:
            print(f"Volo {self.codiceVolo} già prenotato")

    def posti_disponibili(self) -> None:
        return self.nPosti - self.prenotazione
    


class CompagniaAerea:

    def __init__(self, nome: str, prezzo: float) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.flotta: list[VoloCommerciale] = list()


    def aggiungi_volo(self, volo_commerciale: VoloCommerciale):
        if volo_commerciale != None:
            self.flotta.append(volo_commerciale)

    
    def rimuovi_volo(self, volo_commerciale: VoloCommerciale):
        if volo_commerciale in self.flotta:
            self.flotta.remove(volo_commerciale)
        

    def mostra_flotta(self):
        print("Flotta: ")
        for v in self.flotta:
            print(v)

    
    def guadagno(self):

        def _guadagno_volo(volo: VoloCommerciale, prezzo: float):
            tot: float = 0
            tot += round(volo.prenotazioni_economica * prezzo * 1, 2)
            tot += round(volo.prenotazioni_business * prezzo * 2, 2)
            tot += round(volo.prenotazioni_prima * prezzo * 3, 2)
            return tot

        guadagno_totale: float = 0
        for v in self.flotta:
            guadagno_totale += _guadagno_volo(v, self.prezzo)

        return guadagno_totale



with open("report.txt", "w") as f:
    v1 = VoloCommerciale("AA1", 100)
    v2 = VoloCommerciale("AA2", 10)
    print(v1,"\n",v1.posti_disponibili())
    print(v2,"\n",v2.posti_disponibili())
    ca = CompagniaAerea("ryan", 10)
    ca.aggiungi_volo(v1)
    ca.aggiungi_volo(v2)

    v1.prenota_posto(70, "economica")
    print("Guadagno", ca.guadagno())

    print(v1,"\n",v1.posti_disponibili())

    v2.prenota_posto(1,"prima")
    v2.prenota_posto(2,"business")
    v2.prenota_posto(3,"economica")


    ca.mostra_flotta()
    print("Guadagno", ca.guadagno())