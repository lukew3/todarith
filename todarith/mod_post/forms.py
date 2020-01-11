from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug import secure_filename

class PostForm(FlaskForm):
    title = StringField('Title')
    description = StringField('Description')
    photo = StringField('Photo')
    #image = FileField()
    submit = SubmitField('Submit')
