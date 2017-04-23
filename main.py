from model.user import User
from model.beacon import Beacon
import os
from send_mail import send_mail
import json

from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/start', methods=["POST"])
def start():
    email = request.get_json()
    user = {'email': email["mail"]}
    idx = User.make_user(user)

    print(idx)
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


@app.route('/<string:email>/<name>/send')
def send(email, name):
    send_mail(email)
    return redirect(url_for('show_statistics', name=name))


@app.route('/')
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
    products = Beacon.get_products()

    amount = []
    time = []
    for prod in products:
        amount.append({'label': prod[0], 'y': prod[1]})
        time.append({'y': prod[2], 'label': prod[0]})
    amount1 = json.dumps(amount)
    time2 = json.dumps(time)
    print(amount1)
    return render_template("product.html", name=name, products=products, amount=amount1, time=time2)


if __name__ == "__main__":
    app.run(debug=True)