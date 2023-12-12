#!/usr/bin/python3
"""HBNB Flask module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """
    Displays an HTML page with the list of all State objects
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown():
    """
    Close the current session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
