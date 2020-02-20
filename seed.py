from sqlalchemy import func

from model import Artwork, Artist, ArtType, connect_to_db, db
from server import app

from PIL import Image

import os, sys, glob
import urllib.request
from urllib.parse import urlparse
import requests
import json


def read_list_met_obj():
    met_obj_list = []
    with open ("art_obj_id.txt", "r") as obj_file:
        # met_id = obj_file.read().replace("\n", " ")
        for line in obj_file:
            new_line = line.rstrip()
            met_obj_list.append(new_line)
    return met_obj_list


def search_through_url(met_list):

    met_json_list = []

    for met_obj in met_list:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{met_obj}"
        response = requests.get(url)
        json_data = response.json()
        met_json_list.append(json_data)


    # with open('met_list.json', 'w') as f:
    #     f.write(json.dumps(met_json_list))

    return met_json_list


def load_art_types(data):
    """load the art classification"""


    type_code = data.get("classification")

    # ArtType.query.filter(db.not_(ArtType.type_code.in_(type_code)))


    art_type = ArtType(type_code=type_code)

    db.session.merge(art_type)
    db.session.commit()



def load_artists(data):
    """Load artist name from the Met to the database"""

    artist_name = data.get("artistDisplayName")

    art_person = Artist(artist_name=artist_name)

    db.session.add(art_person)
    db.session.commit()


def load_artworks(data):
    """Load the jpg images location from the Met Museum APi to database"""

    art_title = data.get("title")

    art_image_url = data.get("primaryImageSmall")

    # urllib.request.urlretrieve(art_image_url, "static/images/test1")

    art_image_name = urlparse(art_image_url)
    art_image = os.path.basename(art_image_url) # i.e. DT1494.jpg

    img_data = requests.get(art_image_url).content
    with open(f"static/images/{art_image}", 'wb') as handler:
        handler.write(img_data)

    artwork = Artwork(art_title=art_title, 
                      art_image=art_image)

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
    met_list = read_list_met_obj()
    met_json = search_through_url(met_list)

    for data in met_json:
        load_artworks(data)
        load_artists(data)
        load_art_types(data)
    # load_artwork_thumbnails()