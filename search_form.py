from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms.validators import DataRequired, Length 
from flask import Flask

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'orangetoblue'


class SearchForm(FlaskForm):

    tag = StringField('Tag', validators=[DataRequired(), Length(max=20)], render_kw={"placeholder": "tag"})



# class search_artist(Form):
#     artist_search = TextField('search artist,' validators = [DataRequired()])
