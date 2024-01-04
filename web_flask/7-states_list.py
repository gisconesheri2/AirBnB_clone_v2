#!/usr/bin/python3
"""serve State objects"""
from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def get_states():
    """serve the state objects from storage"""
    states_list = []
    states = storage.all(State)
    states_list = states.values()
    return render_template("7-states_list.html", states=states_list)


@app.teardown_appcontext
def close_session(exception):
    """close down current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', threaded=True)
