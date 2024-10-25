from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize
import sys

import dbclient as db


api = Flask(__name__)


cur = db.connect()
if cur is None:
    print("Errore connessione al DB")
    sys.exit()

# file_path = "anagrafe.json"
# cittadini = JsonDeserialize(file_path)

# file_path_users = "utenti.json"
# utenti = JsonDeserialize(file_path_users)



@api.route('/login', methods=['POST'])
def GestisciLogin():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        sUsernameInseritoDalClient = jsonReq["username"]
        sPasswordInseritaDalClient = jsonReq["password"]
        sQuery = "select privilegi from utenti where email='" + sUsernameInseritoDalClient \
            + "' and password='" + sPasswordInseritaDalClient + "';"
        print(sQuery)

        iNumRows = db.read_in_db(cur, sQuery)
        if iNumRows == 0:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
        else:
            myrow = db.read_next_row(cur)
            print(myrow)
            sPriv = myrow[1][0]
            return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio":sPriv}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta errato"}) 
                                             

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        

        user = jsonReq.get('username')
        pw = jsonReq.get('password')
        sQuery = f"select privilegi from utenti where email='{user}' and password='{pw}'"
        iNumRows = db.read_in_db(cur, sQuery)
        if iNumRows == 0:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
        else:
            priv = db.read_next_row(cur)[1][0]


        codice_fiscale = jsonReq.get('codFiscale')
        sQuery = "select * from anagrafe where codice_fiscale='" + codice_fiscale + "';"
        print(sQuery)
        iNumRows = db.read_in_db(cur, sQuery)
        print(iNumRows)
        if iNumRows != 0:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        

        elif priv == 'w':
            sQuery = f"INSERT INTO Anagrafe (codice_fiscale, nome, cognome, data_nascita) \
            VALUES \
            ('{codice_fiscale}', '{jsonReq.get('nome')}', '{jsonReq.get('cognome')}', '{jsonReq.get('dataNascita')}');"
            print(sQuery)
            db.write_in_db(cur, sQuery)
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
        
        else:
            print("privilegio non disponibile")
            return jsonify({"Esito": "002", "Msg": "Privilegio non disponibile"}), 200
        
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




@api.route('/read_cittadino/<codice_fiscale>/<user>/<pw>', methods=['GET'])
def read_cittadino(codice_fiscale, user, pw):
    global cur
    content_type = request.headers.get('Content-Type')
    print(f"{codice_fiscale} - {user} - {pw}")
    if content_type == 'application/json':
        jsonReq = request.json

        user = jsonReq.get('username')
        pw = jsonReq.get('password')
        sQuery = f"select privilegi from utenti where email='{user}' and password='{pw}'"
        iNumRows = db.read_in_db(cur, sQuery)
        if iNumRows == 0:
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
        else:
            priv = db.read_next_row(cur)[1][0]

    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200






@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():

    #prima di tutto verifico utente, password e privilegio 
    #dove utente e password me l'ha inviato il client
    #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200






@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():

    #prima di tutto verifico utente, password e privilegio 
    #dove utente e password me l'ha inviato il client
    #mentre il privilegio lo vado a leggere nel mio file  (utenti.json)
    
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

api.run(host="127.0.0.1", port=8080)

