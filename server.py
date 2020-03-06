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

# UPLOAD_FOLDER = "/static/user_images"
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}
  

app = Flask(__name__)

app.secret_key = "whiteboardsareremarkable"

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.jinja_env.undefined = StrictUndefined

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """Displays homepage."""

    arts = Artwork.query.all()

    return render_template("index.html", arts=arts)


@app.route("/upload")
def upload_image():
    """Displays uploads page"""

    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_submit():
    if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        user_img = file.save(os.path.abspath(f"static/user_images/{filename}"))

        return extract_user_palette(filename)


@app.route("/upload/user-palette")
def extract_user_palette(filename):

    def new_image(mode, size, color):
        return Image.new(mode, size, color)

    file = f"static/user_images/{filename}"

    hai = Haishoku.loadHaishoku(file)
    palette = Haishoku.getPalette(file)

    u_color_pal = []

    for item in palette:
        c_pal = item[1]
        pal = new_image('RGB', (100, 100), c_pal)
        u_color_pal.append(c_pal)

    return render_template("user-palette.html", filename=filename, 
                                                u_color_pal=u_color_pal)


### Attempting Search Function

@app.route("/search") # methods=["GET", "POST"]
def search():

    return render_template("search-form.html")


# @app.route("/search_results/<query>")
# def search_results(query):
#     results = Artworks.query.all()

#     return render_template("search-results.html", query=query)


@app.route("/tags.json") 
def tag_dict():

    tag_info = ArtTag.query.all()
    # Receiving information from the Model.py
    lst_tags = [t.as_dict() for t in tag_info]

    return jsonify(lst_tags)



@app.route("/types.json") 
def type_dict():

    type_info = ArtType.query.all()
    # Receiving information from the Model.py
    lst_type = [t.as_dict() for t in type_info]

    return jsonify(lst_type)
    

# @app.route("/process.json", methods=["POST"])
# def process():
#     tag = request.form["tags.json"]
#     if tag:
#         return jsonify({"text": tag})

#     return jsonify({"error": "missing data"})


@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    art_id = Artwork.query.get(artwork_id)

    return render_template("artwork_detail.html", art_id=art_id)


@app.route("/tags/<tag_code>")
def all_tag(tag_code):
    """When tags are selected in the artwork details page"""

    tag = Tag.query.get(tag_code)

    return render_template("tag_results.html", tag=tag)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")


