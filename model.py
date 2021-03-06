from flask_sqlalchemy import SQLAlchemy 

import sys

db = SQLAlchemy()


class Artist(db.Model):
    """Data on the artist"""

    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False) # try unique=True

    def __repr__(self):
        """Returns artist name as object represenation."""

        return f"<artist name={self.artist_name}>"

    # Casting the object into a dictionary
    # Used for Select2 search boxes
    def as_dict(self):
        return {"id": self.artist_id,
                "text": self.artist_name}


class ArtType(db.Model):
    """Art classification code."""

    __tablename__ = "art_types"

    type_code = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        """Returns the art type."""

        return f"<art type={self.type_code}>"

    def as_dict(self):
        return {"text": self.type_code}


class ArtMedium(db.Model):
    """Art medium/media description."""

    __tablename__ = "art_mediums"

    medium_code = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        """Returns the art type."""

        return f"<art medium={self.medium_code}>"

    def as_dict(self):
        return {"text": self.medium_code}


class Tag(db.Model):
    """ """
    __tablename__ = "tags"

    tag_code = db.Column(db.String, primary_key=True)


class ArtTag(db.Model):
    """Art medium/media description."""

    __tablename__ = "art_tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.artwork_id"))
    tag_code = db.Column(db.String(50), db.ForeignKey("tags.tag_code"))


    def __repr__(self):
        """Returns the art type."""

        return f"<art tag={self.tag_code}>"

    def as_dict(self):
        return {"id": self.tag_id,
                "text": self.tag_code}




class Palette(db.Model):
    """Dominant colors (8) and their precentages."""

    __tablename__ = "palettes"

    color_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    artwork_id = db.Column(db.Integer, db.ForeignKey("artworks.artwork_id"))

    c_percent = db.Column(db.String(50), nullable=False) 
    c_palette = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """ """

        return f"<color palette={self.c_palette}>"


class Artwork(db.Model):
    """Data for an art piece."""

    __tablename__ = "artworks"


    artwork_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    type_code = db.Column(db.String(200), db.ForeignKey("art_types.type_code"))
    medium_code = db.Column(db.String(200), db.ForeignKey("art_mediums.medium_code"))
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"))

    art_type = db.relationship("ArtType", backref="artworks")
    medium_type = db.relationship("ArtMedium", backref="artworks")
    # secondary is calling table name
    tags = db.relationship("Tag", secondary="art_tags", backref="artworks")
    artist = db.relationship("Artist", backref="artworks")
    palette_code = db.relationship("Palette", backref="artworks")

    art_title = db.Column(db.String(200), nullable=False)
    art_image = db.Column(db.String(200), nullable=False) # image url
    art_thumb = db.Column(db.String(200), nullable=False) # image url
    obj_date = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        """Returns art title as object representation."""

        return f"<art title={self.art_title}>"

    def as_dict(self):
        return { "id": self.artwork_id,
                "text": self.art_title}


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
