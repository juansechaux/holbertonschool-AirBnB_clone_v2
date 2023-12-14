#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''Define the main route ("/") with strict_slashes=False option'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Define a new route ("/hbnb") with strict_slashes=False option'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text variable'''
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route("/python/<text>", strict_slashes=False)
@app.route('/python/',strict_slashes=False)
def python_text(text='is cool'):
    '''display “C ” followed by the value of the text variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
