from flask import Flask, render_template, request

utenti = [['mario', 'password1', 'M', 0],['luigi', 'password3', 'M', 0],['luca', 'password2', 'M', 0], ['lucia', 'password4', 'F', 0]]

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
        u_req = []
        u_req.append(request.args.get('username'))
        u_req.append(request.args.get('password'))
        u_req.append(request.args.get('sex'))
        u_req.append(0)
        if u_req[2] == "1":
            u_req[2] = 'M'
        elif u_req[2] == '2':
            u_req[2] = 'F'
        else:
            u_req[2] = 'N'
    print(u_req[:3], " - ", utenti[0][:3])
    for u in utenti:
        if u_req == u:
            u[3] = 1
            return render_template('reg_ok.html')
            
    return render_template('reg_ko.html')

@api.route('/signin', methods=['GET'])
def signin():
    return render_template('signin.html')


@api.route('/login1', methods=['GET'])
def login1():
    if request.method == 'GET':
        u_req = []
        u_req.append(request.args.get('username'))
        u_req.append(request.args.get('password'))

    for u in utenti:
        if u_req == u[:2] and u[3] == 1:
            if u[2] == 'M':
                temp = ' è un maschio'
            else:
                temp = ' è una femmina'
            
            return render_template('user.html')
            
    return render_template('reg_ko.html')


@api.route('/ordiniAttuali', methods=['GET'])
def ordiniAttuali():
    return render_template('ordini-attuali.html')

@api.route('/ordiniPassati', methods=['GET'])
def ordiniPassati():
    return render_template('ordini-passati.html')



api.run(host='0.0.0.0', port=8085)

