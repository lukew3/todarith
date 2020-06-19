from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from todarith.models import User


class AskForm(FlaskForm):
    problem = StringField('Problem')
    answer = StringField('Answer')
    category = StringField('Category')
    submit = SubmitField('Ask')
