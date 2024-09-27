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
        jResponse = {"Error":"000", "Msg": "ok"}
        return json.dumps(jResponse), 200
   
    else: 
        return "Format error", 401



api.run(host="127.0.0.1", port=8080)

