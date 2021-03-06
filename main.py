from model.user import User
from model.beacon import Beacon
import os
from send_mail import send_mail
import json
import ast


from flask import Flask, render_template, request, redirect, url_for, session, jsonify


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
    products = []
    details = []
    picks = User.get_picks_by_email(email)
    for pick in picks:
        print(pick[0], pick[1], pick[2], pick[3])

    for product in picks:
        if product[3] not in products:
            products.append(product[3])


        for cos in products:
            details.append(ast.literal_eval(Beacon.get_product_details(cos)))
        print(products  )
    return render_template("mylist.html", picks=picks, details=details)



@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    Beacon.add_pick(pick["beacon"], pick["mail"])
    import ast
    return jsonify(ast.literal_eval(Beacon.get_beacon_by_uid(pick["beacon"])))


@app.route('/<string:email>/<name>/send')
def send(email, name):
    send_mail(email)
    return redirect(url_for('client_statistics', name=name))


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


@app.route('/buttonsend/',  methods=["POST"])
def send_to():
    send_mail("pgurdek@gmail.com")

    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)