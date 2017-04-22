from model.user import User
from model.beacon import Beacon
import os


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
    Beacon.add_pick(pick)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)