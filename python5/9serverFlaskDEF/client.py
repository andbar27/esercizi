import requests, json, sys

# --------- GLOBAL -----------

host = 'https://127.0.0.1' 
port = 8080
base_url = host + ":" + str(port)


# --------- FUNCTION ---------

def selectOperation() -> str:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")

    op = input("Seleziona Operazione: ")

    return op   

def getDataLogin():
    user = input("Inserisci username: ")
    pw = input("Inserisci password: ")
    dataLogin = {
        "username": user,
        "password": pw
    }
    return dataLogin

def getDataCitizen():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino


def getCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}



def login():
    jsonDataRequest = getDataLogin()
    url = base_url + '/login'

    print(jsonDataRequest)
    response = requests.post(url, json=jsonDataRequest, verify=None)
    if response.status_code == 200:
        jsonDataResponse = response.json()
        print(jsonDataResponse.get('Esito'))
        if jsonDataResponse.get('Esito') == "000":
            user = jsonDataRequest["username"]
            pw = jsonDataRequest["password"]
            priv = jsonDataResponse['privilege']
            print(True, user, pw, priv)
            return True, user, pw, priv
        
        else:
            print(jsonDataResponse.get('Msg'))
            return False, None, None, None
    else:
        return False, None, None, None




# --------- MAIN -------------

successLogin = False
while not successLogin:
    successLogin, user, pw, privilege = login()

jsonDataRequest = {"username": user, "password": pw, "privilege": privilege, "datiCittadino":None}


while True:
    op = selectOperation()

    if op == 1:
        print('Aggiungi cittadino')
        api_url = base_url + "/add_citizen"
        continue

    elif op == 1:
        continue

    elif op == 1:
        continue

    elif op == 1:
        continue

    elif op == 1:
        continue

    else:
        print("Operazione non disponibile, riprova.")