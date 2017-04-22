from model.user import User
from model.beacon import Beacon
import os


from flask import Flask, render_template, request, redirect, url_for, session


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


@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    Beacon.add_pick(pick["beacon"], pick["mail"])
    return render_template("index.html")


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


@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)