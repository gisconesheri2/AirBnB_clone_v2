#!/usr/bin/python3
"""serve State objects"""
from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def get_states_and_cities():
    """serve the state objects from storage"""
    # if os.environ['HBNB_TYPE_STORAGE'] == "db":
    states = storage.all(State)
    states_list = list(states.values())
    return render_template("8-cities_by_states.html", states=states_list)


@app.teardown_appcontext
def close_session(exception):
    """close down current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', threaded=True)
