#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask


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
    if text:
        if '_' in text:
            text.replace('_', ' ')

    return f"C (text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
