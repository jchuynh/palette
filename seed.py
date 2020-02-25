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

    with open("art_obj_id.txt", "r") as obj_file:
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

    artist_duplicate = Artist.query.filter_by(artist_name=artist_name).first()

    if not artist_duplicate:

        art_person = Artist(artist_name=artist_name)

        db.session.add(art_person)
        db.session.commit()
        return art_person.artist_id


    return artist_duplicate.artist_id


def load_art_types(data):
    """load the art classification"""

    type_code = data.get("classification")

    type_duplicate = ArtType.query.get(type_code)

    if not type_duplicate:

        art_type = ArtType(type_code=type_code)

        db.session.add(art_type)
        db.session.commit()

        return art_type.type_code

    return type_duplicate.type_code


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


def load_color_percent(palette):
    """ """

    # file = "static/images//"
    color_per = []

    for item in palette:
    # idx 0 is the percentage of color on the image
        # cannot extend float
        c_percent = item[0]

        color_per.append(c_percent)

    return color_per

    # return Artwork.query(Palette.c_percent).append(Palette(color_per))


def new_image(mode, size, color):
    return Image.new(mode, size, color)


def load_color_palette(c_pal):
    """Create a list of RGB codes and thier percentage of use in artwork"""

    # color_pal = []

    # for item in palette:
        # A tuple of RGB color codes
        # c_pal = item[1]
    pal = new_image('RGB', (100, 100), c_pal)
    file_name = f"static/color_palette/({c_pal}).jpg"
    pal.save(file_name, 'JPEG')

        # color_pal.append(c_pal)

    # return color_pal

    # return Artwork.query(Palette.c_palette).append(Palette(color_pal))


def display_haishoku(art_image, art_id):

    file = f"static/images/{art_image}"

    hai = Haishoku.loadHaishoku(file)
    palette = Haishoku.getPalette(file)

    # c_percent = load_color_percent(palette)
    
    
    for pal in palette:
        load_color_palette(pal[1])
        color = Palette(c_percent=pal[0],
                    c_palette=pal[1],
                    artwork_id=art_id)

        db.session.add(color)
        db.session.commit()

    return color


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
        handler.write(img_data)

    artist_id = load_artists(data)
    type_code = load_art_types(data)
    art_thumb = load_thumbnail(art_image)
    artwork = Artwork(art_title=art_title,
                      art_image=art_piece,
                      art_thumb=art_thumb,
                      artist_id=artist_id,
                      type_code=type_code)

    db.session.add(artwork)
    db.session.commit()
    full_pal = display_haishoku(art_image, artwork.artwork_id)


if __name__ == "__main__":

    connect_to_db(app)
    db.create_all()

    met_list = read_list_met_obj()
    met_json = search_through_url(met_list)

    #maintain a global map

    for data in met_json:
        # load_artists(data)
        # load_art_types(data)
        load_artworks(data)






