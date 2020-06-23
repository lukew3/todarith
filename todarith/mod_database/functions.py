from todarith.models import Problem, Topic, User
from todarith.database import db

def getDBAnswer(query):
    solution = "unavailable"
    print(str(query) + "searched")
    #results=Problem.filter_by(question=searchquery).all()
    result = db.session.query(Problem).filter_by(question=query).first()
    print(result)
    if result != None:
        solution = result.answer
    return solution
