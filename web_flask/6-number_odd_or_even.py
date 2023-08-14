#!/usr/bin/python3
"""
This module defines a simple Flask web application.
"""
from flask import Flask, render_template

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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    This function is executed when the root URL ("/python/<text>") is accessed.
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    This function is executed when the root URL ("number/<n>") is accessed.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    This function is executed when the root URL ("/number_template/<n>")
    is accessed.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    This function is executed when the root URL ("/number_odd_or_even/<n>")
    is accessed.
    """
    if (n % 2) == 0:
        num = f'{n} is even'
    else:
        num = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
