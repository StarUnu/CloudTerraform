from flask import Flask
app = Flask(__name__)
@app.route('/') # el encargado de decirle a Flask qué URL
def hello_world():
    return 'Hello, World!'
