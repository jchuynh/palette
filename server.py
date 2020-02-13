
import jinja2

From flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db


app.secret_key  = 'whiteboardsareremarkable'

app.jinja2_env.undefined = StrictUndefined

##### API #####

# need to save a JSON file
#  

url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'


response = requests.get(url)
data = response.json()

objects = json.dumps(data)

for item in objects:
    





# payload = {'title': art_title,
#            'artistDisplayName': artist_name,
#            'classification': art_media_code,
#            'primaryImageSmall': art_image}



@app.route('/')
def hompage():
    """Displays homepage."""



    return render_template('homepage.html')

@app.route('/artwork/{artwork_id}')
def artwork_detail(artwork_id):
    """Displays more information on single artwork."""

    artwork_id = Artwork.query.get(artwork_id)
    art_title = Artwork.query.get(art_title)
    art_image = Artwork.query.get(art_image)

    return render_template("artwork.html", artwork_id=artwork_id)


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")


