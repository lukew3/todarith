from flask import request, render_template, redirect, url_for, jsonify
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Topic, User
from todarith.mod_database.forms import AskForm
from flask_login import current_user, login_required
from todarith.mod_database import moddb
from todarith.mod_database.functions import getDBAnswer

# Set the route and accepted methods
@moddb.route('/')
def browse():
    return(render_template("database/browse.html"))

@moddb.route('/ask', methods=['GET', 'POST'])
def ask():
    return render_template('database/ask.html')

@moddb.route('/_get_problem_input')
def get_problem_input():
    #print("Somethings")
    prob = request.args.get('problem', "", type=str)
    cat = request.args.get('category', "", type=str)
    print("Problem:" + prob)
    print("Category:" + cat)

    #solved = checkSolved(ans)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    #form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
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
    #return jsonify(result="Problem \"" + prob + "=" + ans + "\" was not added")
    return jsonify(answer="The answer is: " + solution)

@moddb.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('database/add.html')

@moddb.route('/answer', methods=['GET', 'POST'])
def answer():
    unsolved = db.session.query(Problem).filter_by(hasSolution=False).all()
    print(unsolved)
    if unsolved != []:
        problem = unsolved[0]
    else:
        return render_template('database/ask.html')
    print(problem)
    return render_template('database/answer.html', problem=problem)

@moddb.route('/_get_answer_input')
def get_answer_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    print("Problem:" + prob)
    print("Answer:" + ans)

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

    unsolved = db.session.query(Problem).filter_by(hasSolution=False).all()
    if unsolved != []:
        nextProblem = unsolved[0]
    else:
        return render_template('database/ask.html')
    #return jsonify(result="Problem \"" + prob + "=" + ans + "\" was not added")
    return jsonify(problem=nextProblem.question, answer="", category=nextProblem.topic.topicName)
