#This file includes functions that check the validity of a problem
from todarith.models import Problem, Skill

def checkAll(prob, ans):
    if checkEq(prob, ans) and checkRep(prob, ans):
        return True
    else:
        return False

def checkEq(prob, ans):
    solvedAns = eval(prob)
    givenAns = int(ans)
    if(solvedAns==givenAns):
        return True
    else:
        return False

def checkRep(prob, ans):
    print(Problem.query.filter_by(question=prob).all())
    if Problem.query.filter_by(question=prob).all() == []:
        print("Problem already exists")
        return True
    else:
        return False


def checkTopicExists(topic):
    print(Topic.query.filter_by(topicName=topic).all())
    if (Topic.query.filter_by(topicName=topic).all() == []):
        return True
    else:
        return False
