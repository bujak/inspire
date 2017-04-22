from model.user import User
import os
import json


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
    return "user"


@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    print(pick)
    if user:
        user.is_beacon_in_list(id)
    else:
        user = User(mail)
        user.is_beacon_in_list(id)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)