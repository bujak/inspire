from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/receive', methods=["POST"])
def receive():
    pick = request.get_json()
    print(pick)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)