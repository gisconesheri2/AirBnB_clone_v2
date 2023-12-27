"""flask web application handling several routes"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
