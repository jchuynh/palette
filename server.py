from jinja2 import StrictUndefined  

from haishoku.haishoku import Haishoku
from PIL import Image

from flask import Flask, flash, render_template, redirect, jsonify, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename

from model import Artwork, Artist, ArtType, ArtTag, Tag, connect_to_db, db
import upload
# from search_form import SearchForm, connect_to_db, db

# from search_form import SearchForm

import requests
import json 
import os

ALLOWED_EXTENSIONS = {"jpg", "jpeg"} # For user upload
  

app = Flask(__name__)

app.secret_key = "whiteboardsareremarkable"

app.jinja_env.undefined = StrictUndefined


def allowed_file(filename):
    """Check user image upload to determine it uses .jpg or .jpeg"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """Displays homepage"""

    arts = Artwork.query.all()

    return render_template("index.html", arts=arts)


@app.route("/upload")
def upload_image():
    """Displays uploads page"""

    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_submit():
    """User uploading and submitting the image"""
    if 'file' not in request.files: 
            flash('No file part')
            return redirect(request.url)
    file = request.files['file']

    if not file.filename:
    # if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Save the images on the local machine/server
        user_img = file.save(os.path.abspath(f"static/user_images/{filename}"))

        return extract_user_palette(filename)

    return "SOMETHING"


@app.route("/upload/user-palette")
def extract_user_palette(filename):
    """Extracting color palette based on user's image upload"""

    def new_image(mode, size, color):
        """Creating an Image parameters for color analysis"""
        return Image.new(mode, size, color)

    file = f"static/user_images/{filename}"

    hai = Haishoku.loadHaishoku(file)
    palette = Haishoku.getPalette(file)

    u_color_pal = []

    for item in palette:
        c_pal = item[1] # Second item has the RGB codes
        pal = new_image('RGB', (100, 100), c_pal)
        u_color_pal.append(c_pal)

    size = 800, 800 # Size for cropping the user's image for display

    # Open the file from remote and convert to RGB
    im = Image.open(file)
    im.convert("RGB")

    # Use PIL thumbnail method to crop the image
    im.thumbnail(size, Image.ANTIALIAS)

    # Save the file to display on the webpage
    u_crop_img = im.save(file, quality=80)

    return render_template("user-palette.html", filename=filename, 
                                                u_color_pal=u_color_pal, 
                                                u_crop_img=u_crop_img)


@app.route("/search", methods=["GET", "POST"])
def form():

    test = request.args.get("tags")
    data = jsonify(test)

    return render_template("search-form.html", data=data)


    # desriptions = db.session.query(ArtTag).filter_by(tag_code).all()
    # artists = db.session.query(Artist).filter_by(artist_name).all()
    # titles = db.session.query(Artworks).filter_by(artist_title).all()


# @app.route("/search_results/<query>")
# def search_results(query):
#     results = Artworks.query.all()

#     return render_template("search-results.html", query=query)


@app.route("/tags.json") 
def tag_dict():

    tag_info = ArtTag.query.all()

    lst_tags = [t.as_dict() for t in tag_info]

    return jsonify(lst_tags)
    

@app.route("/process", methods=["POST"])
def process():
    tag = request.form["tags.json"]
    if tag:
        return jsonify({"text": tag})

    return jsonify({"error": "missing data"})



@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art_id = Artwork.query.get(artwork_id)

    return render_template("artwork_detail.html", art_id=art_id)


@app.route("/tags/<tag_code>")
def all_tag(tag_code):

    tag = Tag.query.get(tag_code)
    # arts = Artwork.query.all()

    return render_template("tag_results.html", tag=tag)

# @app.route("/title/<title>")
# def all_tag(tag_code):

#     title = Artwork.query.filter_by(art_title)
#     # arts = Artwork.query.all()

#     return render_template("title_results.html", title=title)

# @app.route("/artist/<artist_name>")
# def all_tag(tag_code):

#     artist = Artwork.query.get(tag_code)
#     # arts = Artwork.query.all()

#     return render_template("artist_results.html", artist=artist)

# @app.route("/medium/<medium_code>")
# def all_tag(tag_code):

#     medium = Artwork.query.get(tag_code)
#     # arts = Artwork.query.all()

#     return render_template("medium_results.html", medium=medium)

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


