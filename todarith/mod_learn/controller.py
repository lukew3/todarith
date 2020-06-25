from flask import request, render_template, redirect, url_for, jsonify
from todarith import db
from todarith.models import Problem, Topic, User
from flask_login import current_user, login_required
from todarith.mod_learn import learn
from random import random

# Set the route and accepted methods
@learn.route('/')
def learnHome():
    return(render_template("learn/learnHome.html"))


@learn.route('/practice')
def practice():
    return(render_template("learn/practice.html"))

@learn.route('/practice/_get_problems')
def practice_get_problems():
    allProblems = db.session.query(Problem).all()
    problems = []
    ansCount = request.args.get('ansCount', "", type=int)
    for i in range(ansCount, ansCount+5):
        problems.append(allProblems[i])
    return jsonify(problems=[{'problem': problem.question, 'answer': problem.answer,} for problem in problems])

@learn.route('/practice/_get_problem')
def practice_get_problem():
    unique = False
    usedProb=request.args.get('usedProbs')
    print(usedProb)
    usedProbs = request.args.getlist('usedProbs')
    print(usedProbs)
    allProblems = db.session.query(Problem).all()
    while unique == False:
        problem = allProblems[int(random()*len(allProblems))]
        if str(problem.id) not in usedProbs:
            unique = True
    return jsonify(problem={'problem': problem.question, 'answer': problem.answer, 'id': problem.id})

@learn.route('/practice/_get_answer_input')
def practice_get_answer_input():
    ans = request.args.get('answer', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    return jsonify(answer="The answer is: " + solution)
