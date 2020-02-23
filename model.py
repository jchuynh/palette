from flask_sqlalchemy import SQLAlchemy 

import sys

db = SQLAlchemy()


class Palette(db.Model):
    """ """

    __tablename__ = "palettes"

    color_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.artwork_id"))

    c_percent = db.Column(db.String(50), nullable=False) # not currently utilized
    c_palette = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """ """

        return f"<color palette={self.color_id}>"



class Artist(db.Model):
    """Data on the artist"""

    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False) # try unique=True

    def __repr__(self):
        """Returns artist name as object represenation."""

        return f"<artist name={self.artist_name}>"


class ArtType(db.Model):
    """Art classification code."""

    __tablename__ = "art_types"

    type_code = db.Column(db.String(100), primary_key=True)

    def __repr__(self):
        """Returns the art type."""

        return f"<art type={self.type_code}>"


class Artwork(db.Model):
    """Data for an art piece."""

    __tablename__ = "artworks"


    artwork_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    type_code = db.Column(db.String(200), db.ForeignKey("art_types.type_code"))
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"))

    art_type = db.relationship("ArtType", backref="artworks")
    artist = db.relationship("Artist", backref="artworks")
    full_pal = db.relationship("Palette", backref="artworks")

    art_title = db.Column(db.String(200), nullable=False)
    art_image = db.Column(db.String(200), nullable=False) # image url
    art_thumb = db.Column(db.String(200), nullable=False) # image url



    def __repr__(self):
        """Returns art title as object representation."""

        return f"<art title={self.art_title}>"

#### Helper Functions 

def connect_to_db(app):
    """Connect the data base to our Flask app."""

    # Configure to use PostgreSQL database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///arts"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
        
if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
