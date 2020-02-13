from model import Artwork, connect_to_db, db

from server import app

import requests
import json

def load_artworks():
    """Load the jpg images location from the Met Museum APi to database"""

    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"
    response = requests.get(url)
    data = response.json()

    objects = json.dumps(data)

    art_info = []

    for item in objects:
        art_info_dict = {}
        art_info_dict['art_title'] = data.get('title')
        art_info_dict['art_image'] = data.get('primaryImageSmall')

        art_info.append(art_info_dict)

        for ele in art_info:
            print(ele)

    artwork= Artwork(art_title=art_title, 
                     art_image=art_image)

    db.session.add(artwork)

    db.session.commit()

# def load_artits():
#     """Load artist name from the Met to the database"""

if __name__ == "__main__":
    connect_to_db(app)

    load_artworks()