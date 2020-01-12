from datetime import datetime
from flask import current_app
from todarith import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}' )"

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
"""
