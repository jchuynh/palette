from jinja2 import StrictUndefined  

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import Artwork, Artist, ArtType, connect_to_db, db

# from image_resize import resize_image

import requests
import json 
  

app = Flask(__name__)

app.secret_key = "whiteboardsareremarkable"

app.jinja_env.undefined = StrictUndefined

# url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
# response = requests.get(url)
# data = response.json() 


@app.route("/")
def index():
    """Displays homepage."""

    images = db.session.query(Artwork).order_by("art_image").all()
    titles = db.session.query(Artwork).order_by("art_title").all()
    art_id = Artwork.query.get(artwork_id).all()

    return render_template("index.html", images=images,
                                         titles=titles)

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art_id = Artwork.query.get(artwork_id)


    return render_template("artwork_detail.html", artwork=artwork)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


