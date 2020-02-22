import os, sys, glob, urllib.request, json, requests

from sqlalchemy import func

from model import Artwork, Artist, ArtType, Palette, connect_to_db, db
from server import app

from haishoku.haishoku import Haishoku
from PIL import Image
from urllib.parse import urlparse


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


def load_artists(data):
    """Load artist name from the Met to the database"""

    artist_name = data.get("artistDisplayName")

    art_person = Artist(artist_name=artist_name)

    db.session.merge(art_person) # used merge so duplicates won't be an issue.
    db.session.commit()

def load_art_types(data):
    """load the art classification"""


    type_code = data.get("classification")

    art_type = ArtType(type_code=type_code)

    db.session.merge(art_type) # used merge so duplicates won't be an issue.
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

    art_piece = f"static/images/{art_image}"

    # write and save the image file into the folder with the basename
    with open(art_piece, 'wb') as handler:
        img_path = handler.write(img_data)


    art_thumb = load_thumbnail(art_image)
    c_pall = display_haishoku(art_image)

    artwork = Artwork(art_title=art_title, 
                      art_image=art_piece,
                      art_thumb=art_thumb)


    db.session.add(artwork)
    db.session.commit()


def load_thumbnail(art_image):
    """Load resized images (thumbnails)"""

    file = f"static/images/{art_image}"

    size = 350, 350

    im = Image.open(file)
    im.convert("RGB")
    im.thumbnail(size, Image.ANTIALIAS)

    thumb_path = f"static/thumbnails/{art_image}_thumb.jpg"

    im.save(thumb_path, 'JPEG', quality=80)

    return thumb_path


def display_haishoku(art_image):

    file = f"static/images/{art_image}"

    hai = Haishoku.loadHaishoku(file)
    palette = Haishoku.getPalette(file)

    c_percent = load_color_percent(palette)
    c_palette = load_color_palette(palette)

    color = Palette(c_percent=c_percent, 
                    c_palette=c_palette)

    db.session.add(color)
    db.session.commit()


def load_color_percent(palette):
    """ """

    file = "static/images//"

    color_per = []

    for item in palette:
    # idx 0 is the percentage of color on the image
        c_percent = item[0]

        color_per.append(c_percent)

    return color_per

def new_image(mode, size, color): 
    return Image.new(mode, size, color)


def load_color_palette(palette):
    """Create a list of RGB codes and thier percentage of use in artwork"""

    color_pal = []

    for item in palette:
        # A tuple of RGB color codes
        c_pal = item[1]
        pal = new_image('RGB', (100, 100), c_pal)
        file_name = f"static/color_palette/({c_pal}).jpg"
        pal.save(file_name, 'JPEG')

        color_pal.append(c_pal)

    return color_pal


    # artwork.palletes.append(Palette(djflksjfl))
    # commit

            


if __name__ == "__main__":

    connect_to_db(app)
    db.create_all()

    met_list = read_list_met_obj()
    met_json = search_through_url(met_list)


    for data in met_json:
        load_artists(data)
        load_art_types(data)
        load_artworks(data)









