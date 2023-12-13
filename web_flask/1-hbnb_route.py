#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask


# Create an instance of the Flask application
app = Flask(__name__)


# Define the main route ("/") with strict_slashes=False option
@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''Define the main route ("/") with strict_slashes=False option'''
    return "Hello HBNB!"


# Define a new route ("/hbnb") with strict_slashes=False option
@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    '''Define a new route ("/hbnb") with strict_slashes=False option'''
    return "HBNB"


# Check if the script is being run as the main program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
