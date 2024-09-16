from flask import Flask, render_template, request

utenti = [['mario', 'password1'],['luigi', 'password3'],['luca', 'password2']]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('reg_ko.html')

@api.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        user = request.args.get('username')
        pw = request.args.get('password')

    for u in utenti:
        if user == u[0]:
            if pw == u[1]:
                return render_template('reg_ok.html')
            
    return render_template('reg_ko.html')


api.run(host='0.0.0.0', port=8085)

