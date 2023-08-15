#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """After each request this removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    return render_template('7-states_list.html', states=storage.all(State))


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    return render_template('9-states.html',
                           states=storage.all(State).get(
                               'State.{}'.format(id)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
