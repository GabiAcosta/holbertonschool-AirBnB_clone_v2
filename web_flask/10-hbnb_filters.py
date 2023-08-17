#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """After each request this removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    return render_template('10-hbnb_filters.html', states=storage.all(State),
                           amenities = storage.all(Amenity))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
