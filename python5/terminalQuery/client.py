import requests, json, sys

base_url = "http://127.0.0.1:8080"


def EseguiOperazione(iOper, api_url, jsonDataRequest):
    try:
        if iOper == 1 or iOper == 2:
            response = requests.post(api_url, json=jsonDataRequest)
            
        if response.status_code == 200:
            print("Esito: ", response.json()["Esito"])
            print("Msg: ", response.json()["Msg"], "\n")
            print("risultato query: ")
            print(response.json()["queryResult"])
        else:
            print("Attenzione, errore " + str(response.status_code))
            print(response.json())

    except:
        print("Problemi comunicazione con il server")


def getQuery() -> str :
    query = input("Inserisci Query (';' per terminare): \n")
    while query[-1] != ';':
        query = query + "\n" + input()
    print(query)
    return {"query": query}

"""
"INSERT INTO Anagrafe (codice_fiscale, nome, cognome, data_nascita) 
    VALUES ('f', 'f', 
    'f', '2000-01-01');"
"""



print("Benvenuti nel Database")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Query lettura")
    print("2. Query scrittura")
    print("3. Esci")
    
    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if iOper == 1:
        print("Query lettura")
        jsonDataRequest = getQuery()
        api_url = base_url + "/readquery"
        EseguiOperazione(1, api_url, jsonDataRequest)

    elif iOper == 2:
        print("Query scrittura")
        jsonDataRequest = getQuery()
        api_url = base_url + "/writequery"
        EseguiOperazione(2, api_url, jsonDataRequest)
    
    elif iOper == 3:
        print("Chiusura programma")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")

