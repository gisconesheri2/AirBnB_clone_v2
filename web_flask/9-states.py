#!/usr/bin/python3
"""serve State objects"""
from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states_with_no_id():
    """serve the state objects from storage"""
    id_given = 0
    states = storage.all(State)
    states_list = list(states.values())
    return render_template("9-states.html", states=states_list, id_given=0)


@app.route("/states/<id>")
def states_with_id(id):
    """serve the state object with given id from storage"""
    states = storage.all(State)
    key_name = f"State.{id}"
    state_with_id = states.get(key_name, None)
    return render_template("9-states.html", states=state_with_id, id_given=1)


@app.teardown_appcontext
def close_session(exception):
    """close down current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', threaded=True)
