from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug import secure_filename

class QuestionForm(FlaskForm):
    question = StringField('Question')
    answer = StringField('Answer')
    classNumber = StringField('Class')
    section = StringField('Section')
    type = StringField('Type')
    #photo = StringField('Photo')
    #image = FileField()
    submit = SubmitField('Submit')
