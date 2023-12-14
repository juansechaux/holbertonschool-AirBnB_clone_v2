#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask
from flask import render_template

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
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    '''display “Python ”, followed by the value of the text variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def n_int(n):
    '''display “n is a number” only if n is an integer'''
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_n_int(n):
    '''display “n is a number” only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_and_odd(n):
    if n % 2 == 0:
        total = 'even'
    else:
        total = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, total=total)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)