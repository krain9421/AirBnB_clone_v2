#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.run(host="0.0.0.0")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns the text `Hello HBNB!`
    """
    return ("Hello HBNB!")
