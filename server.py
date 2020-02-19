from jinja2 import StrictUndefined  

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import Artwork, Artist, ArtType, connect_to_db, db

import requests
import json 
  

app = Flask(__name__)

app.secret_key = "whiteboardsareremarkable"

app.jinja_env.undefined = StrictUndefined

# url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
# response = requests.get(url)
# data = response.json() 


##### API #####

# url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
# response = requests.get(url)
# data = response.json()

# objects = json.dumps(data)


@app.route("/")
def index():
    """Displays homepage."""

    art_title = Artwork.query.first()

    artwork = Artwork.query.first() # gives an object

    return render_template("index.html", artwork=artwork)

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art_id = Artwork.query.get(artwork_id)
    # artwork = Artwork.query.all()

    return render_template("artwork_detail.html", artwork=artwork)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


