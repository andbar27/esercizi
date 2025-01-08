import requests, json, sys
from flask import Flask, render_template, request

base_url = "http://127.0.0.1:8080"

client_url = "http://127.0.0.1:8085"

api = Flask(__name__)



@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/nav', methods=['GET'])
def nav():
    return render_template('nav.html')


@api.route('/marketing', methods=['GET'])
def marketing():
    return render_template('marketing.html')




@api.route('/cerca_affitto', methods=['GET'])
def cerca_affitto():
    return render_template('cerca_affitto.html')


@api.route('/res_affitto', methods=['POST'])
def res_affitto():
    jsonRequest = dict()
    jsonRequest['indirizzo'] = request.form.get('indirizzo', '')
    jsonRequest['prezzo'] = request.form.get('prezzo', '0')
    jsonRequest['bagno'] = request.form.get('bagno', 'False')
    jsonRequest['stato'] = request.form.get('stato', '')
    print("Form:")
    print(jsonRequest)
    res_data = None

    try:
        api_url = base_url + '/elenco_case_affitto'
        response = requests.post(api_url, json=jsonRequest)
        jsonResponse = response.json()
        if jsonResponse["Esito"] == "000":
            print(jsonResponse["Res"])
            res_data = jsonResponse["Res"] 



    except:
        print("Attenzione, problemi di comunicazione con il server\n")

    return render_template('res_affitto.html', res_data = res_data)




@api.route('/cerca_vendita', methods=['GET'])
def cerca_vendita():
    return render_template('cerca_vendita.html')

@api.route('/res_vendita', methods=['POST'])
def res_vendita():
    jsonRequest = dict()
    jsonRequest['indirizzo'] = request.form.get('indirizzo', '')
    jsonRequest['prezzo'] = request.form.get('prezzo', '0')
    jsonRequest['metri'] = request.form.get('metri', '0')
    jsonRequest['stanze'] = request.form.get('stanze', '0')
    jsonRequest['stato'] = request.form.get('stato', '')
    print("Form:")
    print(jsonRequest)
    res_data = None

    try:
        api_url = base_url + '/elenco_case_vendita'
        response = requests.post(api_url, json=jsonRequest)
        jsonResponse = response.json()
        if jsonResponse["Esito"] == "000":
            print(jsonResponse["Res"])
            res_data = jsonResponse["Res"] 



    except:
        print("Attenzione, problemi di comunicazione con il server\n")

    return render_template('res_vendita.html', res_data = res_data)


@api.route('/inserisci_affitto', methods=['GET'])
def inserisci_affitto():
    return render_template('inserisci_affitto.html')


@api.route('/res_ins_affitto', methods=['POST'])
def res_ins_affitto():
    jsonRequest = dict()
    jsonRequest['catastale'] = request.form.get('catastale', '')
    jsonRequest['filiale'] = request.form.get('filiale', '')
    jsonRequest['indirizzo'] = request.form.get('indirizzo', '')
    jsonRequest['civico'] = request.form.get('civico', '')
    jsonRequest['prezzo'] = request.form.get('prezzo', '0')
    jsonRequest['bagno'] = request.form.get('bagno', 'False')
    jsonRequest['stato'] = request.form.get('stato', '')
    print("Form:")
    print(jsonRequest)
    res_data = None

    try:
        api_url = base_url + '/inser_affitto'
        response = requests.post(api_url, json=jsonRequest)
        jsonResponse = response.json()
        if jsonResponse["Esito"] == "000":
            print(jsonResponse["Res"])
            res_data = jsonResponse["Res"] 



    except:
        print("Attenzione, problemi di comunicazione con il server\n")

    return index()




api.run(host='0.0.0.0', port=8085)


