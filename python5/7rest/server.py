from flask import Flask, json, request
from myjson import SerializeJson, DeserializeJson

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_citizen', methods=['POST'])
def addCitizen():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata "+ content_type)

    if content_type == "application/json":
        jRequest = request.json
        print(jRequest)
        # Carichiamo la anagrafe
        dAnagrafe: dict = DeserializeJson(sFileAnagrafe)
        sCodiceFiscale = jRequest["codice fiscale"]
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            SerializeJson(dAnagrafe, sFileAnagrafe)

            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale già presente"}
            return json.dumps(jResponse), 500 
        
   
    else: 
        return "Format error", 401



@api.route('/data_citizen', methods=['POST'])
def dataCitizen():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata "+ content_type)

    if content_type == "application/json":
        jRequest = request.json
        print(jRequest)
        # Carichiamo la anagrafe
        dAnagrafe: dict = DeserializeJson(sFileAnagrafe)
        sCodiceFiscale = jRequest["codice fiscale"]
        if sCodiceFiscale in dAnagrafe:
            data_citizen = dAnagrafe[sCodiceFiscale]

            jResponse = {"Error":"000", "Msg": "ok"}
            jResponse.update(data_citizen)
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale non presente"}
            return json.dumps(jResponse), 500 
        
   
    else: 
        return "Format error", 401
    


@api.route('/modify_citizen', methods=['POST'])
def modCitizen():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata "+ content_type)

    if content_type == "application/json":
        jRequest = request.json
        print(jRequest)
        # Carichiamo la anagrafe
        dAnagrafe: dict = DeserializeJson(sFileAnagrafe)
        sOldCF = jRequest["old_cf"]
        sCodiceFiscale = jRequest["codice fiscale"]
        if sOldCF in dAnagrafe:
            dAnagrafe.pop(sOldCF)   # rimuovo vecchio dict con chiave cf_old
            jRequest.pop("old_cf")  # rimuovo old_cf dal dizionario da aggiungere
            dAnagrafe[sCodiceFiscale] = jRequest # aggiungo nuovo dict con cf aggiornato
            SerializeJson(dAnagrafe, sFileAnagrafe)

            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale non presente"}
            return json.dumps(jResponse), 500 
        
   
    else: 
        return "Format error", 401
    


@api.route('/remove_citizen', methods=['POST'])
def rmCitizen():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata "+ content_type)

    if content_type == "application/json":
        jRequest = request.json
        print(jRequest)
        # Carichiamo la anagrafe
        dAnagrafe: dict = DeserializeJson(sFileAnagrafe)
        sCodiceFiscale = jRequest["codice fiscale"]
        if sCodiceFiscale in dAnagrafe:
            dAnagrafe.pop(sCodiceFiscale)
            SerializeJson(dAnagrafe, sFileAnagrafe)

            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale non presente"}
            return json.dumps(jResponse), 500 
        
   
    else: 
        return "Format error", 401





api.run(host="127.0.0.1", port=8080)

