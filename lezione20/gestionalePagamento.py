class Pagamento:

    def __init__(self) -> None:

        self.importo = None

    def getImporto(self) -> float:
        return self.importo
    
    def setImporto(self, importo) -> None:
        self.importo = round(importo, 2)

    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{round(self.importo, 2)}")


class PagamentoContanti(Pagamento):

    def inPezziDa(self) -> list[float]:

        importo = round(self.importo, 2)
        banconote = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
        pezziDa = []

        i = 0
        while importo != 0:
            
            if importo - banconote[i] >= 0:
                importo = round(importo - banconote[i], 2)
                pezziDa.append(banconote[i])

            else:
                i += 1

        print(pezziDa)
        
        numeroPezziDa: dict[str][int] = dict()
        for pezzi in pezziDa:

            if pezzi not in numeroPezziDa:
                numeroPezziDa[pezzi] = 1

            else:
                numeroPezziDa[pezzi] += 1
        
        print(numeroPezziDa)
        return numeroPezziDa
    
    def dettagliPagamento(self):

        print(f"Pagamento in contanti di: €{round(self.importo, 2)}")
        
        print(f"{round(self.importo, 2)} euro da pagare in contanti con:")
        

        banconote: dict[str][int] = self.inPezziDa()
        for key, value in banconote.items():
            tipo = "banconota"
            if float(key) < 1:
                tipo = "moneta"

            if value > 1:
                tipo = tipo[::-1].replace("a","e")[::-1]

            print(f"{value} {tipo} da {key} euro")

    

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome, data_scadenza, numero_carta) -> None:
        super().__init__()
        self.nome: str = nome
        self.data_scadenza: str = data_scadenza
        self.numero_carta: str = numero_carta


    def dettagliPagamento(self):

        print(f"Pagamento di: €{round(self.importo,2)} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")
        


pc1 = PagamentoContanti()
pc1.setImporto(1125.29)
print(f"get: {pc1.getImporto()}")
pc1.dettagliPagamento()

print("\n")

pcc1 = PagamentoCartaDiCredito("Gino Paoli", "27/06", "2222222222")
pcc1.setImporto(625)
print(f"get: {pcc1.getImporto()}")
pcc1.dettagliPagamento()

print("\n")

p1 = Pagamento()
p1.setImporto(225)
p1.dettagliPagamento()

