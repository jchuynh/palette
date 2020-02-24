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

    arts = Artwork.query.all()

    # t_images = db.session.query(Artwork).order_by("art_thumb").all()
    # titles = db.session.query(Artwork).order_by("art_title").all()

    return render_template("index.html", arts=arts)

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art_id = Artwork.query.get(artwork_id)
    # arts = Artwork.query.all()


    return render_template("artwork_detail.html", art_id=art_id)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


