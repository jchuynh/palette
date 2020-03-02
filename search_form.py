from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length 
from flask import Flask

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'orangetoblue'


class SearchForm(FlaskForm):

    search = StringField("search", validators=[DataRequired(), Length(max=20)], render_kw={"placeholder": "search"})
    submit = SubmitField("search", render_kw={"class": "btn btn-success btn-block"})


# class search_artist(Form):
#     artist_search = TextField('search artist,' validators = [DataRequired()])
