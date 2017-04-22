from model.user import User
from model.beacon import Beacon
import os
from send_mail import send_mail
import json

from flask import Flask, render_template, request, redirect, url_for, session,jsonify


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/start', methods=["POST"])
def start():
    email = request.get_json()
    user = {'email': email["mail"]}
    idx = User.make_user(user)
    # user["id"] = idx
    print(idx)
    # session['user'] = user
    # print(session['user'])
    return ""


@app.route('/<string:email>/mylist')
def mylist(email):
    picks = User.get_picks_by_email(email)
    for pick in picks:
        print(pick[0])
    return render_template("mylist.html", picks=picks)


@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    Beacon.add_pick(pick["beacon"], pick["mail"])
    return render_template("index.html")


@app.route('/<string:email>/send')
def send(email):
    send_mail(email)
    return "Email send"


@app.route('/business/login', methods=['POST', 'GET'])
def b_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form["login"]
        print(name)
        user = {'firm': name}
        session['user'] = user
        # Here shoul be some logic for checking password
        return redirect(url_for('show_statistics', name=name))


@app.route('/business/<name>')
def show_statistics(name):
    return render_template("index.html", name=name)


@app.route('/business/<name>/global')
def global_statistics(name):
    clients = User.get_clients()
    amount = []
    time = []
    for client in clients:
        amount.append({'label': client[0], 'y': client[2]})
        time.append({'label': client[0], 'y': client[1]})
    amount1 = json.dumps(amount)
    time2 = json.dumps(time)

    return render_template("global.html", name=name, clients=clients, amount=amount1, time=time2)


@app.route('/business/<name>/client')
def client_statistics(name):
    clients = User.sigle_client()
    amount = []
    time = []
    for client in clients:
        amount.append({'label': client[0], 'y': client[1]})
        time.append({'label': client[0], 'y': client[2]})
    amount1 = json.dumps(amount)
    time2 = json.dumps(time)

    return render_template("client.html", name=name, clients=clients, amount=amount1, time=time2)


@app.route('/business/<name>/product')
def product_statistics(name):
    return render_template("product.html", name=name)


@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)