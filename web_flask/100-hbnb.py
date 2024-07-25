#!/usr/bin/python3
"""
Starts a Flask web application for the HBNB project.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb URL.
    Renders the HBNB main page.
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
