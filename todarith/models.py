from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from todarith.database import db, CRUDMixin
from app.extensions import bcrypt
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
    problems = db.relationship('Problem', backref='poster', lazy=True)
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
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) #user id of the person who posted it
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
        return f"Problem('{self.question}', '{self.answer}', '{self.topic}')"


class Topic(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String(100), nullable=False)
    problems = db.relationship('Problem', backref='topic', lazy=True)
    parentTopic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    subtopics = db.relationship('Topic', backref=db.backref('parentTopic', remote_side=[id]), lazy=True)


"""
class CustomList(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listName = db.Column(db.String(100), nullable=False)
    problems = db.Column(db.String(100), nullable=False) # should be array with references to problems
"""
