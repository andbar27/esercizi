"""Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati."""
def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    retDict: dict = dict()
    for key, value in dizionario.items():
        if value not in retDict:
            retDict[value] = key
    return retDict
    
"""Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3."""
def somma_condizionale(numeri: list[int]) -> int :
    condition = [2,3]
    somma = 0
    for n in numeri:
        if(n % 2 == 0) and (n % 3 == 0):
            somma += n
    return somma

"""Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
    Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori."""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for key, value in da_rimuovere.items():
        for i in range(value):
            if key in lista:
                lista.remove(key)
    return lista

"""Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario."""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    retDict: dict[str:list[int]] = dict()
    for voto in voti:
        nome = ""
        for key, value in voto.items():
            if key == 'nome':
                nome = value
                if nome not in retDict:
                    retDict[nome] = []
            elif key == 'voto':
                retDict[nome].append(value)
    return retDict

"""Scrivi una funzione che accetti un dizionario di prodotti con i prezzi 
    e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%."""
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    retDict: dict = dict()
    for key, value in prodotti.items():
        if value > 20:
            retDict[key] = value - (value / 10)
    return retDict

"""
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare.
Questa funzione dovrebbe aggiornare il dizionario del contatto.
"""
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    return {'profile': name, 'email': email, 'telefono': telefono}
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if name != dictionary['profile']:
        return dictionary
    if email != None:
        dictionary['email'] = email
    if telefono != None:
        dictionary['telefono'] = telefono
    return dictionary
