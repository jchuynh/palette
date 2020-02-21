from sqlalchemy import func

from model import Artwork, Artist, ArtType, connect_to_db, db
from server import app
from haishoku.haishoku import Haishoku
from PIL import Image

# from image_resize import resize_image
# from color_extract import new_image, create_color_palette

import os, sys, glob, urllib.request, json
from urllib.parse import urlparse
import requests


def read_list_met_obj():
    """Read the object ids from a txt file"""

    met_obj_list = []
    with open ("art_obj_id.txt", "r") as obj_file:
        for line in obj_file:
            new_line = line.rstrip()
            met_obj_list.append(new_line)

    return met_obj_list


def search_through_url(met_list):
    """Add the JSON data into a list"""

    met_json_list = []

    for met_obj in met_list:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{met_obj}"
        response = requests.get(url)
        json_data = response.json()
        met_json_list.append(json_data)

    return met_json_list


def load_art_types(data):
    """load the art classification"""


    type_code = data.get("classification")

    art_type = ArtType(type_code=type_code)

    db.session.merge(art_type) # used merge so duplicates won't be an issue.
    db.session.commit()



def load_artists(data):
    """Load artist name from the Met to the database"""

    artist_name = data.get("artistDisplayName")

    art_person = Artist(artist_name=artist_name)

    db.session.merge(art_person) # used merge so duplicates won't be an issue.
    db.session.commit()


def load_artworks(data):
    """Load the jpg images location from the Met Museum APi to database"""

    art_title = data.get("title")

    # url from the Met API
    art_image_url = data.get("primaryImageSmall")

    # rename the image as the base id given
    # i.e. DT1494.jpg
    art_image = os.path.basename(art_image_url)

    # get the content from the art_image_url
    img_data = requests.get(art_image_url).content

    # write and save the image file into the folder with the basename
    with open(f"static/images/{art_image}", 'wb') as handler:
        img_path = handler.write(img_data)

    artwork = Artwork(art_title=art_title, 
                      art_image=art_image)


    db.session.add(artwork)
    db.session.commit()

    return img_path

def load_thumbnail(img_path):
    """Load resized images (thumbnails)"""

    size = 350, 350

    # for art_image in dirs:
    if os.path.isfile(img_path):
        # if art_image == '.DS_Store': 
        #     continue
        im = Image.open(img_path)
        im.convert('RGB')
        im.thumbnail(size, Image.ANTIALIAS)

        thumb_path = f"static/thumbnails/{ art_image }_thumb.jpg"

        art_thumb = os.path(thumb_path)
        print(art_thumb)

        im.save(thumb_path, 'JPEG', quality=80)

        thumb_art = Artwork(art_thumb=art_thumb)
               

        db.session.add(thumb_art)
        db.session.commit()


def return_haishoku(img_path):
    hai = Haishoku.loadHaishoku(img_path)
    palette = Haishoku.getPalette(img_path)

    return palette


def load_color_palette(palette):
    """Create a list of RGB codes and thier percentage of use in artwork"""

    color_pal = []

    for item in palette:
        # idx 0 is the percentage of color on the image
        c_percent = item[0]
        # A tuple of RGB color codes
        c_pal = item[1]

        color_pal.append(c_pal)


        color_palette = Artwork(color_pal=color_pal)
               
        db.session.add(color_palette)
        db.session.commit()
    

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    met_list = read_list_met_obj()
    met_json = search_through_url(met_list)

    for data in met_json:
        load_artworks(data)
        load_artists(data)
        load_art_types(data)
