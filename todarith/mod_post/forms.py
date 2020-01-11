from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from werkzeug import secure_filename


classChoices=[('1', 'kindergarten'), ('2', 'first grade'), ('3', 'second grade')]

class QuestionForm(FlaskForm):
    question = StringField('Question')
    answer = StringField('Answer')
    #classNumber = StringField('Class')

    classNumber = SelectField('Class', choices = classChoices)
    section = StringField('Section')
    type = StringField('Type')
    #photo = StringField('Photo')
    #image = FileField()
    submit = SubmitField('Submit')
