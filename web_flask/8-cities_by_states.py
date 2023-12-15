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
    # Obtener todos los objetos State
    states = storage.all(State).values()

    # Ordenar los estados alfabéticamente por el atributo 'name'
    sorted_states = sorted(states, key=lambda state: state.name)

    # Crear un diccionario de estados ordenados
    dict_states = {state.id: state for state in sorted_states}

    # Se ordernan las ciudades de la a-z
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    dict_cities = {city.id: city for city in sorted_cities}

    return render_template('8-cities_by_states.html',
                           dict_states=dict_states, dict_cities=dict_cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
