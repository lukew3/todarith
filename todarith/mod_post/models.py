from datetime import datetime
from todarith import db, login_manager
from flask_login import UserMixin

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
