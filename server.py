import urllib.request
import requests
import json
import os
import collections

from haishoku.haishoku import Haishoku
from PIL import Image

from flask import Flask, flash, render_template, redirect, jsonify, request, url_for, session, make_response
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename

from model import Artwork, Artist, ArtType, ArtTag, Tag, connect_to_db, db

from jinja2 import StrictUndefined  


# Allowed extensions for users to upload images
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}

app = Flask(__name__)

app.secret_key = "app.secret_key" # Exporting from secrets.sh

app.jinja_env.undefined = StrictUndefined


# @app.route("/")
# def index():
#     """Displays homepage."""
()
#     arts = Artwork.query.all()

#     return render_template("index.html", arts=arts)

@app.route("/index")
def display_all_artworks():
    """Displays all available artworks."""
    arts = Artwork.query.all()

    return render_template("index.html", arts=arts)


@app.route("/upload")
def upload_image():
    """Displays uploads page"""

    return render_template("upload.html")


def allowed_file(filename):
    """Uploading image ans securing filename."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    """Display user image and color palette."""

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


@app.route("/search-form", methods=["GET"])
def user_search():
    """Populate the search-box."""

    return render_template("search-form.html")


@app.route("/search")
def user_search_1():

    search = request.args.get("term")

    return render_template("search-form.html", search=search)


@app.route("/search-results", methods=["GET", "POST"])
def search_items():
    """Displays search results based on user selection."""

    user_input = request.args.get("text")

    results = None

    # Querying into database to obtain the 3 search categories.
    tag = Tag.query.filter_by(tag_code=user_input).first()
    artist = Artist.query.filter_by(artist_name=user_input).first()
    title = Artwork.query.filter_by(art_title=user_input).first()

    # When user submits selection in search-box, check if they are in the
    # following categories
    if tag:
        results = {'type': 'tag',
                   'artworks': []}
        for artwork in tag.artworks:
            results['artworks'].append({'url': artwork.art_thumb,
                                        'art_id': artwork.artwork_id})

    if artist:
        results = {'type': 'artist',
                   'artworks': []}
        for artwork in artist.artworks:
            results['artworks'].append({'url': artwork.art_thumb,
                                        'art_id': artwork.artwork_id})

    if title:
        results = {'type': 'title',
                   'url': title.art_thumb,
                   'art_id': title.artwork_id}

    return jsonify(results)


@app.route("/search-test", methods=["GET", "POST"])
def all_query():
    """Sending JSON object with all the search queries."""
    
    # Get the serach term selected by user
    term = request.args.get("term")

    artists = Artist.query.filter(Artist.artist_name.ilike(f'%{term}%')).all()
    artist_search = {"text": "Artist Name", "children": [{"id": artist.artist_id,
                     "text": artist.artist_name} for artist in artists]}

    tags = ArtTag.query.filter(ArtTag.tag_code.ilike(f'%{term}%')).all()
    tag_search = {"text": "Tags (descriptions)", "children": [{"id": tag.tag_id, 
                  "text": tag.tag_code} for tag in tags]}

    titles = Artwork.query.filter(Artwork.art_title.ilike(f'%{term}%')).all()
    title_search = {"text": "Artwork Titles", "children": [{"id": artwork.artwork_id, 
                    "text": artwork.art_title} for artwork in titles]}

    results = []

    results.append(artist_search)
    results.append(tag_search)
    results.append(title_search)

    return jsonify({"results": results})


@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    # Get the art id to display information about each piece.
    artwork = Artwork.query.get(artwork_id)

    if 'visit' not in session:
        session['visit'] = []

    if artwork.artwork_id not in session['visit']:
        session['visit'].append(artwork.artwork_id)
    session.modified = True

    # List to hold Artwork id's
    data = []

    # Get the visit dictionary out of the session or an empty one.
    visit = session.get('visit', {})

    # Loop over the visit dictionary
    for artwork_id in session['visit']:

        # Get the Artwork Object corresponding to this id
        site = Artwork.query.get(artwork_id)

        # Add Artwork object to list
        data.append(site)

    # When the items in the list is greater than 5, remove the first recently 
    # visited items
        if(len(data) > 5):
            data.pop(0)


    return render_template("artwork_detail.html",
                           visit=data,
                           art_id=artwork)


@app.route("/tags/<tag_code>")
def all_tag(tag_code):
    """When tags are selected in the artwork details page"""

    tag = Tag.query.get(tag_code)

    return render_template("tag_results.html", tag=tag, tag_code=tag_code)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
