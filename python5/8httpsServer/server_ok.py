from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)

file_path = "utenti.json"
utenti = JsonDeserialize(file_path)

@api.route('/login', methods=['POST'])
def Login():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        jsonReq = request.json
        user = jsonReq.get('username')
        pw = jsonReq.get('password')
        
        if user in utenti and utenti[user]["password"] == pw:
            return jsonify({"Esito": "000", "Msg": "Login ok", "privilege": utenti[user]["privilegi"]}), 200
        
        else:
            return jsonify({"Esito": "001", "Msg": "Username o password errati"}), 200
    
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if request.json.get('privilege') != 'w':
            return jsonify({"Esito": "003", "Msg": "Privilegi non sufficienti"}), 200

        jsonReq = request.json.get('datiCittadino')
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200






@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if request.json.get('privilege') != 'w':
            return jsonify({"Esito": "003", "Msg": "Privilegi non sufficienti"}), 200

        jsonReq = request.json.get('datiCittadino')
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
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':

        if request.json.get('privilege') != 'w':
            return jsonify({"Esito": "003", "Msg": "Privilegi non sufficienti"}), 200

        cod = request.json.get('datiCittadino').get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

api.run(host="127.0.0.1", port=8080)

