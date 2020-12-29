from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from todarith.database import db, CRUDMixin
from todarith.extensions import bcrypt
import uuid

class User(CRUDMixin, db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    pw_hash = db.Column(db.String(500), unique=False, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=True)
    problems = db.relationship('Problem', backref='poster', lazy=True)
    #profilePicture = db.Column(db.String(20), unique=False, nullable=False, default="default.jpg")

    def __init__(self, username, email, pw_hash):
        self.username = username
        self.email = email
        self.pw_hash = pw_hash

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"


skillproblems = db.Table('skillproblems',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

class Skill(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skillName = db.Column(db.String(100), nullable=False)
    problems = db.relationship(
        "Problem",
        secondary=skillproblems,
        back_populates="skills")

    def __repr__(self):
        return f"Skill('{self.id}', '{self.skillName}', '{self.problems}')"
        #return f"Problem('{self.id}', '{self.skillName}', '{self.problems}')"

setproblems = db.Table('setproblems',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True),
    db.Column('set_id', db.Integer, db.ForeignKey('set.id'), primary_key=True)
)


class Set(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setName = db.Column(db.String(100), nullable=False)
    problems = db.relationship('Problem', secondary=setproblems, lazy='subquery',
        backref=db.backref('sets', lazy=True))


class Problem(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) #user id of the person who posted it
    correctnessRating = db.Column(db.Integer, nullable=False)
    sortRating = db.Column(db.Integer, nullable=False)
    difficultyLevel = db.Column(db.String(1000), nullable=True)
    expectedTime = db.Column(db.String(1000), nullable=True)
    hasSolution = db.Column(db.Boolean(), nullable=False)
    skills = db.relationship(
        "Skill",
        secondary=skillproblems,
        back_populates="problems")
    #source = db.Column(db.String(1000), nullable=True)
    #explanation = db.Column(db.String(10000), nullable=True)

    def __repr__(self):
        return f"Problem('{self.question}', '{self.answer}')"
