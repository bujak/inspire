from model.user import User
from model.beacon import Beacon
import os
from send_mail import send_mail

from flask import Flask, render_template, request, session


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
    user["id"] = idx
    print(idx)
    session['user'] = user
    print(session['user'])
    return


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


if __name__ == "__main__":
    app.run(debug=True)