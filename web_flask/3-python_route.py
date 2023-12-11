#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays a basic Hello world type message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route(f'/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Display formatted text after "C "
    """
    text = text.replace("_", " ")
    # HTML escaping to prevent injection
    return f"C {escape(text)}"


@app.route(f'/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route(f'/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Display formatted text after "Python "
    """
    text = text.replace("_", " ")
    # HTML escaping to prevent injection
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
