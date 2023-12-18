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


@app.route("/states", strict_slashes=False)
def states_list():
    """/states_list route"""
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda x: x.name)
    states_filter = 0
    return render_template('9-states.html',
                           states=states_list, states_filter=states_filter)


@app.route("/states/<id>", strict_slashes=False)
def state_filter(id):
    # Obtener todos los objetos State
    states = storage.all(State).values()
    # key = "State." + id
    # if key in states:
    for state in states:
        if state.id == id:
            cities = storage.all(City).values()
            sorted_cities = sorted(cities, key=lambda city: city.name)
            dict_cities = {city.id: city for city in sorted_cities}
            states_filter = 1
            return render_template('9-states.html', state=state,
                                   states_filter=states_filter,
                                   dict_cities=dict_cities)
        else:
            continue
    states_filter = 2
    return render_template('9-states.html', states_filter=states_filter)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
