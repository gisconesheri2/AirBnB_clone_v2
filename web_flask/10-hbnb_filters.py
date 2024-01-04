#!/usr/bis/python3
"""serve State objects"""
from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False
static_url_path = '/static'


@app.route("/hbnb_filters")
def serve_hbnb():
    """serve the state objects from storage"""
    states = storage.all(State)
    sta = states.values()
    amenities = storage.all(Amenity)
    amen = amenities.values()
    return render_template("10-hbnb_filters.html", states=sta, amenities=amen)


@app.teardown_appcontext
def close_session(exception):
    """close down current database session"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', threaded=True)
