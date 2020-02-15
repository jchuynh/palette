from jinja2 import StrictUndefined  

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import Artwork, Artist, ArtType, connect_to_db, db

import requests
import json 
  

app = Flask(__name__)

app.secret_key = "whiteboardsareremarkable"

# url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
# response = requests.get(url)
# data = response.json() 


##### API #####

# url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
# response = requests.get(url)
# data = response.json()

# objects = json.dumps(data)


# def get_data():

#     art_info = []

#     for item in objects:
#         art_info_dict = {}

#         art_info_dict['art_title'] = data.get('title')
#         art_info_dict['artist_name'] = data.get('artistDisplayName') 
#         art_info_dict['art_image'] = data.get('primaryImageSmall')
#         art_info_dict['type_code'] = data.get('classification')
#         art_info.append(art_info_dict)
#     return art_info



@app.route("/")
def index():
    """Displays homepage."""

    art_title = Artwork.query.first() # gives object

    return render_template("index.html", art_title=art_title)

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art = Artwork.query.get(artwork_id)

    art.artwork_id
    art.tilt
    return render_template("artwork.html", artwork_id=artwork_id)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


