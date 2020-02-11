from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from todarith.models import Problem;
from todarith.models import User, Problem, Topic
from todarith.database import db
from todarith.mod_post.controller import getTopics

#topicChoices=[('1', 'Addition'), ('2', 'Subtraction'), ('3', 'Multiplication')]


class QuestionForm(FlaskForm):

    @classmethod
    def topicChoices():
        return [(row.id, row.topicName) for row in Topic.query.all()]

    question = StringField('Question')
    answer = StringField('Answer')
    topic = SelectField('Class', choices=topicChoices())
    submit = SubmitField('Add')


class TopicForm(FlaskForm):
    #add some way to add parent or child topics
    topicName = StringField('Topic Name')
    submit = SubmitField('Submit')
