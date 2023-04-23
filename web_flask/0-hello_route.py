"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    Returns the text `Hello HBNB!`
    """
    return ("Hello HBNB!")
