from flask import Flask, jsonify, request
from myjson import JsonSerialize, JsonDeserialize

host = '127.0.0.1'
port = 8080

api = Flask(__name__)

file_path = 'users.json'
users = JsonDeserialize(file_path)

@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonRequest = request.json
        user = jsonRequest.get('username')
        pw = jsonRequest.get('password')

        if user in users and users[user]['password'] == pw:
            priv = users[user]['privilege']
            return jsonify({"Esito": "000", "Msg": "Login ok", "privilege": priv}), 200 

        else:
            return jsonify({"Esito": "001", "Msg": "Username o password errati"}), 200
        
    else:
        return jsonify({"Esito": "002", "Msg": "Fromato richista non valido"}), 200




file_path = 'anagrafe.json'
cittadini = JsonDeserialize(file_path)

@api.route('/add_citizen', methods=['POST'])
def addCitizen():
    pass






api.run(host=host, port=port, ssl_context="adhoc")