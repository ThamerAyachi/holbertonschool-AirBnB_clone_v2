#!/usr/bin/python3
"""Simple application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """Refresh data"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ return all cities in the db  """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
