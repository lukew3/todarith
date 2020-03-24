#This file includes functions that check the validity of a problem
from todarith.models import Problem, Topic

def checkAll(prob, ans):
    if checkRep(prob, ans): # and checkEq(prob, ans)
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

def checkOriginal(prob, ans):
    #print(Problem.query.filter_by(question=prob).all())
    if Problem.query.filter_by(question=prob).all() == []:
        return True
    else:
        print("Problem already exists")
        return False


def checkTopicExists(topic):
    print(Topic.query.filter_by(topicName=topic).all())
    if (Topic.query.filter_by(topicName=topic).all() == []):
        return True
    else:
        return False

def checkSpam(prob, ans):
    #Not necessary yet since no word problems
    #should be ai, learns from set of "problems", with vulgar language or other content that shouldn't appear in a math problem
    pass

def checkSolved(ans):
    if ans!="":
        return True
    else:
        return False
