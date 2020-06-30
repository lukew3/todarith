from flask import request, render_template, redirect, url_for, jsonify
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Topic, User
from todarith.mod_database.forms import AskForm
from flask_login import current_user, login_required
from todarith.mod_database import moddb
from todarith.mod_database.functions import getDBAnswer
from random import random

# Set the route and accepted methods
@moddb.route('/')
def browse():
    return(render_template("database/browse.html"))



@moddb.route('/ask', methods=['GET', 'POST'])
def ask():
    return render_template('database/ask.html')

@moddb.route('/ask/_get_problem_input')
def ask_get_problem_input():
    prob = request.args.get('problem', "", type=str)
    cat = request.args.get('category', "", type=str)
    print("Problem:" + prob)
    print("Category:" + cat)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    dbAns = getDBAnswer(prob)
    print(dbAns)
    solution = dbAns
    if dbAns=="unavailable":
        Problem.create(
            question=prob,
            answer="unsolved",
            topic_id=1,
            poster_id=poster,
            correctnessRating=0,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=False
        )
    return jsonify(answer="The answer is: " + solution)



@moddb.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('database/add.html')

@moddb.route('/add/_get_problem_input')
def add_get_problem_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    cat = request.args.get('category', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    if db.session.query(Problem).filter_by(question=prob).first() != None:
        return jsonify(result="Duplicate Found")
    else:
        Problem.create(
            question=prob,
            answer=ans,
            topic_id=1,
            poster_id=poster,
            correctnessRating=0,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=True
        )
        return jsonify(result="Problem " + prob + " added")




@moddb.route('/answer', methods=['GET', 'POST'])
def answer():
    unsolved = db.session.query(Problem).filter_by(hasSolution=False).all()
    if unsolved != []:
        randIndex = int(random()*(len(unsolved)))
        print(randIndex)
        problem = unsolved[randIndex]
    else:
        return render_template('database/ask.html')
    return render_template('database/answer.html', problem=problem)

def getUnsolvedProb():
    unsolved = db.session.query(Problem).filter_by(hasSolution=False).all()
    if unsolved != []:
        randIndex = int(random()*(len(unsolved)))
        print(randIndex)
        nextProblem = unsolved[randIndex]
    else:
        return render_template('database/ask.html')
    return jsonify(problem=nextProblem.question, answer="", category=nextProblem.topic.topicName)

@moddb.route('/answer/_get_answer_input')
def get_answer_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    currentProblem = db.session.query(Problem).filter_by(question=prob).first()
    currentProblem.update(
        answer = ans,
        hasSolution = True,
        correctnessRating = currentProblem.correctnessRating + 1
    )
    return getUnsolvedProb()

@moddb.route('/answer/_flag_problem')
def flag_problem():
    prob = request.args.get('problem', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    currentProblem = db.session.query(Problem).filter_by(question=prob).first()
    currentProblem.update(
        correctnessRating = currentProblem.correctnessRating - 1
    )
    return getUnsolvedProb()

@moddb.route('/answer/_skip_problem')
def skip_problem():
    return getUnsolvedProb()
