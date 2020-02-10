from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#classChoices=[('1', 'Kindergarten'), ('2', 'First Grade'), ('3', 'Second Grade')]
class QuestionForm(FlaskForm):
    question = StringField('Question')
    answer = StringField('Answer')
    topic = SelectField('Class')
    submit = SubmitField('Submit')


class TopicForm(FlaskForm):
    #add some way to add parent or child topics
    topicName = StringField('Topic Name')
    submit = SubmitField('Submit')
