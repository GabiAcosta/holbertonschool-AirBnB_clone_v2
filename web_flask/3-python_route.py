#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    This function is executed when the root URL ("/") is accessed.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function is executed when the root URL ("/hbnb") is accessed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    This function is executed when the root URL ("/c/<text>") is accessed.
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={ 'text': 'is cool' })
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    This function is executed when the root URL ("/python/<text>") is accessed.
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
