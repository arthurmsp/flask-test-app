from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!!!</p>"

@app.route('/oi')
def oi_mundo():
    return "<p>Oi, mundo!!!</p>"