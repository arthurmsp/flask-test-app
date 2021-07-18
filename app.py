from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!!!</p>"

@app.route('/oi')
def oi_mundo():
    return "<p>Oi, mundo!!!</p>"

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method=='POST':
        return 'Invalid Method. Please use GET'
    else:
        name = request.args.get('name')
        age = request.args.get('age')
        response = {
            'name':name,
            'age':age
            }
        return response

