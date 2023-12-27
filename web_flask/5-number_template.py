#!/usr/bin/python3
"""flask web application handling several routes"""
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """the landing page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_alone():
    """for the /hbnb route"""
    return "HBNB"


@app.route("/c/<text>")
def c_shout_out(text):
    """accept arguments in the url passed into flask and print out a message"""
    shout_out = text.replace("_", " ")
    return f"C {escape(shout_out)}"


@app.route("/python")
def lonely_python():
    """for the /python route"""
    return "Python is cool"


@app.route("/python/<text>")
def python_shout_out(text):
    """accept arguments in the url passed into flask and print out a message"""
    shout_out = text.replace("_", " ")
    return f"Python {escape(shout_out)}"


@app.route("/number/<int:n>")
def numbers_only(n):
    """accept only integer arguments in the url passed
    into flask and print out a message
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """render html template for the number given"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
