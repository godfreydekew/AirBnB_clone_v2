#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Main route which displays text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Main route which displays text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Main route which displays text"""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
