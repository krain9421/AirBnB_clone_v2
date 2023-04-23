#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.run(host="0.0.0.0:5000")
def hello_hbnb():
    """
    Returns the text `Hello HBNB!`
    """
    return ("Hello HBNB!")
