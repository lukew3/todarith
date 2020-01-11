from todarith import db

class Problem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    #probNumofType = db.Column(db.Integer)
    question = db.Column(db.String(1000), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    #Not sure if this should be a number or a name, number could have a name that renders after displayed and name might take extra space
    classNumber = db.Column(db.Integer, nullable=False)
    section = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable =False)
