#!/usr/bin/python3
"""HBNB Flask module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states():
    """
    Displays an HTML page with the list of all State objects
    """
    states_list = storage.all(State)

    return render_template("9-states.html", states=states_list, state_id=id)


@app.teardown_appcontext
def teardown():
    """
    Closes the current session after the each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
