from flask import request, render_template, redirect, url_for, jsonify
from todarith import db
from todarith.models import Problem, Skill, User
from flask_login import current_user, login_required
from todarith.mod_learn import learn
from random import random

# Set the route and accepted methods
@learn.route('/')
def learnHome():
    return(render_template("learn/learnHome.html"))


@learn.route('/practice')
def practice():
    skills = Skill.query.filter_by().all()
    return(render_template("learn/practice.html", skills=skills))


@learn.route('/practice/_get_problem')
@learn.route('/practice/_get_problem/<int:skillId>')
def practice_get_problem(skillId):
    unique = False
    usedProb=request.args.get('usedProbs')
    usedProbs = request.args.getlist('usedProbs')
    skill = Skill.query.filter_by(id=skillId).first()
    allProblems = skill.problems
    print(allProblems)
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

@learn.route('/practice/_skill_select')
def practice_skill_select():
    skillId = request.args.get('skillId', 1, type=int)
    #skillname = request.args.get('skillname', '', type=string)
    return practice_get_problem(skillId)
