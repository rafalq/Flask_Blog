from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class SearchForm(FlaskForm):
    search = StringField('Find By Title', validators=[DataRequired(), Length(max=60)])
    submit = SubmitField('Search')
