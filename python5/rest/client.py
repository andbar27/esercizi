import json, requests, sys

base_url = "http://127.0.0.1:8080"

def createInterface():
    print("Operazioni disponibili")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina Cittadino")
    print("5. Exit")


def setDataCitizen():
    nome = input("inserisci nome: ")
    cognome = input("inserisci cognome: ")
    data = input("inserisci data: ")
    cf = input("inserisci codicefiscale: ")
    jRequest = {"nome":nome, "cognome":cognome, "dataNascita":data, "codFiscale":cf}
    return jRequest

createInterface()
selectedOp = input("Seleziona operazione: ")

while (selectedOp != "5"):
    
    if selectedOp == "1":
        api_url = base_url + "/add_citizen"
        jsonDataRequest = setDataCitizen()

        try: 
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Comunication problems with the server")
    

    elif selectedOp == "2":
        continue
    
    elif selectedOp == "3":
        continue
    
    elif selectedOp == "4":
        continue

    createInterface()
    selectedOp = input("Seleziona operazione")

sys.exit()