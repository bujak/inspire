from model.user import User
from model.beacon import Beacon
import os
from send_mail import send_mail
import json
import ast

from flask import Flask, render_template, request, redirect, url_for, session, jsonify


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

# s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
# json_acceptable_string = s.replace("'", "\"")
# d = json.loads(json_acceptable_string)

@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    Beacon.add_pick(pick["beacon"], pick["mail"])
    import ast
    return jsonify(ast.literal_eval(Beacon.get_beacon_by_uid(pick["beacon"])))


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
    client_amount = 1
    return render_template("global.html", name=name)


@app.route('/business/<name>/client')
def client_statistics(name):
    return render_template("client.html", name=name)


@app.route('/business/<name>/product')
def product_statistics(name):
    return render_template("product.html", name=name)


@app.route('/buttonsend/',  methods=["POST"])
def send_to():
    send_mail("pgurdek@gmail.com")

    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)