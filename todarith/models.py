from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from todarith.database import db, CRUDMixin
"""from todarith import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""

class User(CRUDMixin, db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"


class Problem(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    #should either be a boolean that says if confirmed or not or be a number
    #maybe be a number that says how many people have confirmed correct
    confirmedCorrect = db.Column(db.String(1000), nullable=True)#should be nullable=False
    #The problems difficulty level, not sure how that will be judged, maybe by students independently
    difficultyLevel = db.Column(db.String(1000), nullable=True) #time in minutes, could be intervals of 1,2,3,5,10,15
    # The expected time to solve if basic understanding is assumed
    #could be judged by how long students spend on the page until it is solved
    #make sure that they are active and extra long data is not included
    expectedTime = db.Column(db.String(1000), nullable=True)
    #other tags can be included like AP style, conceptual, application, or word problem
    otherTags = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Problem('{self.question}', '{self.answer}')"


class Topic(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String(100), nullable=False)
    #next columnshould be a list of topic id's that belong underneath the topic
    #ex. calculus is main topic and differentiation is a subTopic
    subTopics = db.Column(db.String(100), nullable=False)
    #next col should be a list of problems that belong directly to the topic and don't fall into subtopic category
    problems = db.Column(db.String(100), nullable=False)

"""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    photo = db.Column(db.String(1000), nullable=False, unique=False)
    #author =
    #photo =

    def __repr__(self):
        return f"Post('{self.title}', '{self.description}')"

class Problem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    #probNumof = db.Column(db.Integer)
    question = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    #Not sure if this should be a number or a name, number could have a name that renders after displayed and name might take extra space
    classNumber = db.Column(db.Integer, nullable=False)
    section = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.Integer, nullable =False)

    def __repr__(self):
        return f"Problem('{self.question}', '{self.answer}' )"

class Classnum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    className = db.Column(db.String(100), nullable=False)

    sections = db.relationship('Section', backref='classnum', lazy=True)
    #classnum.sections to get a list of all sections that belong to class

    def __repr__(self):
        return f"Classnum('{self.id}', '{self.className}' )"

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(100), nullable=False)

    class_id = db.Column(db.Integer, db.ForeignKey('classnum.id'))
    topics = db.relationship('Topic', backref='section', lazy=True)
    #parent = #classNum

    def __repr__(self):
        return f"Section('{self.id}', '{self.section}' )"

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    #parent = Section

    def __repr__(self):
        return f"Topic('{self.id}', '{self.topic}' )"
"""
