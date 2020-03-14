from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from todarith.models import Problem
from todarith.database import db

class ProblemSearchForm(Form):
    submission = StringField('Search for:')
    submit = SubmitField('Search')
