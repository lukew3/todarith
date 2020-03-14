from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from todarith.models import Problem
from todarith.database import db

class ProblemSearchForm(FlaskForm):
    submission = StringField('Search for:')
    submit = SubmitField('Search')
