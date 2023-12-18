#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def clean_up_all(exc):
    '''Función de limpieza que se ejecutará al
    finalizar el contexto de la aplicación'''
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """/states_list route"""
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda x: x.name)
    city_list = list(storage.all(City).values())
    city_list.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html',
                           states=states_list, cities=city_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
