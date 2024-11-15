import requests, json, sys
from flask import Flask, render_template, request

base_url = "http://127.0.0.1:8080"

client_url = "http://127.0.0.1:8085"

api = Flask(__name__)


def responseHTML(jsonField):
    return render_template('response.html', jsonField=json.dumps(jsonField, indent=4))


@api.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@api.route('/login', methods=['POST'])
def login():
    global sUsername, sPassword, sPrivilegio

    sUsername = request.form['username']

    sPassword = request.form['password']

    jsonRequest = {"username":sUsername, "password":sPassword}

    try:
        #manda i dati al server
        api_url = base_url + "/login"
        response = requests.post(api_url,json=jsonRequest)
        
        
        #processa la risposta del server
        if response.status_code==200:
            jsonResponse = response.json()
            if jsonResponse["Esito"]=="000":
                sPrivilegio = jsonResponse["Privilegio"]
                iPrimoLoginEffettuato = 1
                print(response.json(), "\n")
                return select_operation()

    except:
        print("Attenzione, problemi di comunicazione con il server\n")


    print(response.json(), "\n")
    return render_template('log_ko.html')

@api.route('/select_operation', methods=['GET'])
def select_operation():
    return render_template('select_operation.html')


@api.route('/insert_cit', methods=['GET'])
def insert_cit():
    return render_template('insert_cit.html')

@api.route('/r_insert_cit', methods=['POST'])
def r_insert_cit():
    api_url = base_url + "/add_cittadino"
    jsonDataRequest = GetDatiCittadino()
    sRes = EseguiOperazione(1, api_url, jsonDataRequest)
    return responseHTML(sRes)


@api.route('/view_cit', methods=['GET'])
def view_cit():
    return render_template('view_cit.html')

@api.route('/r_view_cit', methods=['GET'])
def r_view_cit():
    api_url = base_url + "/read_cittadino"
    jsonDataRequest = GetCodicefiscale()
    res = EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'] + "/" + jsonDataRequest['username'] + "/" + jsonDataRequest['password'],None)
    return responseHTML(res)


@api.route('/edit_cit', methods=['GET'])
def edit_cit():
    return render_template('edit_cit.html')

@api.route('/r_edit_cit', methods=['POST'])
def r_edit_cit():
    api_url = base_url + "/update_cittadino"
    jsonDataRequest = updateDatiCittadino()
    sRes = EseguiOperazione(3, api_url, jsonDataRequest)
    return responseHTML(sRes)




@api.route('/delete_cit', methods=['GET'])
def delete_cit():
    return render_template('delete_cit.html')


@api.route('/r_delete_cit', methods=['POST'])
def r_delete_cit():
    print("Eliminazione cittadino")
    api_url = base_url + "/elimina_cittadino"
    jsonDataRequest = GetCodicefiscale()
    sRes = EseguiOperazione(4, api_url, jsonDataRequest)
    return responseHTML(sRes)





def GetDatiCittadino():
    global sUsername, sPassword
    
    nome = request.form['nome']
    cognome = request.form['cognome']
    dataN = request.form['data_nascita']
    codF = request.form['codFiscale']
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF,
        "username": sUsername,
        "password": sPassword
    }
    return datiCittadino

def updateDatiCittadino():
    global sUsername, sPassword

    cf_old = request.form['old_codFiscale']
    nome = request.form['nome']
    cognome = request.form['cognome']
    dataN = request.form['data_nascita']
    codF = request.form['codFiscale']
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF,
        "username": sUsername,
        "password": sPassword,
        "cf_old": cf_old
    }
    return datiCittadino


def GetCodicefiscale():
    global sUsername, sPassword, sPrivilegio
    if request.method == 'GET':
        cod = request.args.get('codFiscale')
    else:
        cod = request.form['codFiscale']
    datiCittadino = {
        "codFiscale": cod,
        "username": sUsername,
        "password": sPassword
    }
    return datiCittadino


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            return response.json()
        else:
            return "Attenzione, errore " + str(response.status_code)
    except:
        return "Problemi di comunicazione con il server, riprova più tardi."


api.run(host='0.0.0.0', port=8085)