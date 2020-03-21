from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from todarith.database import db, CRUDMixin
from todarith.extensions import bcrypt


class User(CRUDMixin, db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    pw_hash = db.Column(db.String(500), unique=False, nullable=False)
    problems = db.relationship('Problem', backref='poster', lazy=True)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __init__(self, username, email, pw_hash):
        self.username = username
        self.email = email
        self.pw_hash = pw_hash

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"


class Topic(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String(100), nullable=False)
    problems = db.relationship('Problem', backref='topic', lazy=True)
    parentTopic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=True)
    subtopics = db.relationship('Topic', backref=db.backref('parentTopic', remote_side=[id]), lazy=True)

    def __repr__(self):
        return f"Problem('{self.id}', '{self.topicName}')"


clistproblems = db.Table('clistproblems',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True),
    db.Column('customList_id', db.Integer, db.ForeignKey('customlist.id'), primary_key=True)
)


class Customlist(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listName = db.Column(db.String(100), nullable=False)
    problems = db.relationship('Problem', secondary=clistproblems, lazy='subquery',
        backref=db.backref('customLists', lazy=True))


class Problem(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) #user id of the person who posted it
    confirmedCorrect = db.Column(db.String(1000), nullable=True)
    difficultyLevel = db.Column(db.String(1000), nullable=True)
    expectedTime = db.Column(db.String(1000), nullable=True)
    #otherTags = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"Problem('{self.question}', '{self.answer}', '{self.topic}')"
