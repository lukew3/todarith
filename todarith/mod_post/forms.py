from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from todarith.models import Problem;
from todarith.models import User, Problem, Topic
from todarith.database import db

#topicChoices=[('1', 'Addition'), ('2', 'Subtraction'), ('3', 'Multiplication')]
#topicChoices = [('1', 'Addition'), ('2', 'Subtraction'), ('3', 'Multiplication')]
class QuestionForm(FlaskForm):
    question = StringField('Question')
    answer = StringField('Answer')
    topic = SelectField('Class')
    submit = SubmitField('Add')


class TopicForm(FlaskForm):
    #add some way to add parent or child topics
    topicName = StringField('Topic Name')
    #parentTopic = SelectField('Parent Topic')
    submit = SubmitField('Submit')
