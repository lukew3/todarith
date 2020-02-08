from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#classChoices=[('1', 'Kindergarten'), ('2', 'First Grade'), ('3', 'Second Grade')]

class QuestionForm(FlaskForm):
    question = StringField('Question')
    answer = StringField('Answer')
    classNumber = SelectField('Class')
    section = SelectField('Section')
    topic = SelectField('Topic')
    #photo = StringField('Photo')
    #image = FileField()
    submit = SubmitField('Submit')

class BranchForm(FlaskForm):
    parentBranch = SelectField('Parent Branch')
    branchName = StringField('New Branch Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
