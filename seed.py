from sqlalchemy import func

from model import Artwork, Artist, ArtType, connect_to_db, db
from server import app

from PIL import Image

import os, sys, glob
from urllib.parse import urlparse
import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"

def load_art_types():
    """load the art classification"""

    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
    response = requests.get(url)
    data = response.json() 

    type_code = data.get("classification")

    art_type = ArtType(type_code=type_code)

    db.session.add(art_type)
    db.session.commit()



def load_artists():
    """Load artist name from the Met to the database"""

    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
    response = requests.get(url)
    data = response.json()

    artist_name = data.get("artistDisplayName")

    art_person = Artist(artist_name=artist_name)

    db.session.add(art_person)
    db.session.commit()


def load_artworks():
    """Load the jpg images location from the Met Museum APi to database"""

    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
    response = requests.get(url)
    data = response.json()

    # objects = json.dumps(data)

    # for item in objects:
    art_title = data.get("title")

    art_image_url = data.get("primaryImageSmall")

    art_image_name = urlparse(art_image_url)
    art_image = os.path.basename(art_image_url) # i.e. DT1494.jpg


    artwork = Artwork(art_title=art_title, 
                      art_image=art_image)

    print('hello')

    db.session.add(artwork)
    db.session.commit()

# def load_artwork_thumbnails():
#     """Processing resizing of images"""

#     size = 350, 350

#     thumb_path = f"static/thumbnails/{ art_image }.jpg"

#     im = Image.open(url)
#     im.convert('RGB')
#     im.thumbnail(size, Image.ANTIALIAS)
#     im.save(thumb_path, 'JPEG')

#     artwork = Artwork(art_thumb=art_thumb)

#     db.session.add(artwork)
#     db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_artworks()
    load_artists()
    load_art_types()
    # load_artwork_thumbnails()