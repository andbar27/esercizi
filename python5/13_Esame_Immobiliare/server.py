from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize
import sys

import dbclient as db


api = Flask(__name__)


cur = db.connect()
if cur is None:
    print("Errore connessione al DB")
    sys.exit()



@api.route('/elenco_case_vendita', methods=['POST'])
def elenco_case_vendita():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        prezzo = ' prezzo <= ' + jsonReq.get('prezzo')
        indirizzo = ' indirizzo like \'%' + jsonReq.get('indirizzo') + '%\''
        metri = ' metri >= ' + jsonReq.get('metri') 
        stato = ' stato = \'' + jsonReq.get('stato') + '\''
        stanze = ' vani >= ' + jsonReq.get('stanze')
        _and = ' and '
        query = 'select * from case_in_vendita where ' + prezzo + _and \
        + indirizzo + _and + metri + _and + stato + _and + stanze + ';'
        print(query)
        iNumRows = db.read_in_db(cur, query)
        res = []
        for i in range(iNumRows):
            res.append(db.read_next_row(cur))
        print(res)
        return jsonify({"Esito": "000", "Msg": "Ok", "Res": res})
    
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido", "Res": []})






##############  AFFITTO!!!



@api.route('/elenco_case_affitto', methods=['POST'])
def elenco_case_affitto():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        prezzo = ' prezzo_mensile <= ' + jsonReq.get('prezzo')
        indirizzo = ' indirizzo like \'%' + jsonReq.get('indirizzo') + '%\''
        bagno = ' bagno_personale is ' + jsonReq.get('bagno') 
        stato = ' tipo_affitto = \'' + jsonReq.get('stato') + '\''
        _and = ' and '
        query = 'select * from case_in_affitto where ' + prezzo + _and \
        + indirizzo + _and + bagno + _and + stato + ';'
        print(query)
        iNumRows = db.read_in_db(cur, query)
        res = []
        for i in range(iNumRows):
            res.append(db.read_next_row(cur))
        print(res)
        return jsonify({"Esito": "000", "Msg": "Ok", "Res": res})
    
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido", "Res": []})

#############

'''
INSERT INTO case_in_affitto (catastale, indirizzo, civico, tipo_affitto, 
bagno_personale, prezzo_mensile, filiale_proponente) VALUES
('D111', 'Via Torino', 15, 'TOTALE', TRUE, 1200.00, '01234567890'),
('E222', 'Via Genova', 20, 'PARZIALE', FALSE, 800.00, '09876543210'),
('F333', 'Viale Bologna', 7, 'TOTALE', TRUE, 1500.00, '11223344556');
'''

@api.route('/inser_affitto', methods=['POST'])
def inser_affitto():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        query = 'INSERT INTO case_in_affitto (catastale, indirizzo, civico, tipo_affitto, bagno_personale, prezzo_mensile, filiale_proponente) VALUES('
        catastale = '\'' + jsonReq.get('catastale') + '\','
        indirizzo = '\'' + jsonReq.get('indirizzo') + '\','
        civico = jsonReq.get('civico') + ','
        tipo_affitto = '\'' + jsonReq.get('stato') + '\','
        bagno_personale = '\'' + jsonReq.get('bagno') + '\','
        prezzo = jsonReq.get('prezzo') + ','
        filiale = '\'' + jsonReq.get('filiale') + '\''
        query += catastale + indirizzo + civico + tipo_affitto + bagno_personale + prezzo + filiale + ');'
        print(query)
        res = db.write_in_db(cur, query)
        if res == 0:
            return jsonify({"Esito": "000", "Msg": "Ok", "Res": res})
        else:
            return jsonify({"Esito": "001", "Msg": "Error Insert", "Res": res})
    
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido", "Res": []})




api.run(host="127.0.0.1", port=8080)