#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route("/", strict_slashes=False)
def hello():
    """Main route which displays text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Main route which displays text"""
    return "HBNB"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Renders a simple html page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_odd(n):
    """Renders a simple html page"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
