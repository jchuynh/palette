from flask_sqlalchemy import SQLAlchemy 


db = SQLALchemy()


class Artwork(db.Model):
    """Data for an art piece."""

    __tablename__ = "artworks"

    artwork_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    art_title = db.Column(db.String(100), nullable=False)
    art_image = db.Column(db.String(300), nullable=False) # URL of the image.
    # color_pal = db.Column(db.) Type of data the color palette should be

    def __repr__(self):
        """Returns art title as object representation."""

        return f"<art title={self.art_title}>"


class Artist(db.Model):
    """Data on the artist"""

    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    artist_name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Returns artist name as object represenation."""

        return f"<artist name={self.artist_name}>"


class TypeCode(db.Model):
    """Art classification code."""

    __tablename__ = "type_codes"

    type_code = db.Column(db.Integer)

    def __repr__(self):
        """Returns the art type."""

        return f"<art type={self.type_code}>"

#### Helper Functions 

def connect_to_db(app):
    """Connect the data base to our Flask app."""

    # Configure to use PostgreSQL database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///ratings"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Falsedb.app = app
    db.init_app(app)
        

