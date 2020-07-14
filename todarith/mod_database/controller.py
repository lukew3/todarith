from flask import request, render_template, redirect, url_for, jsonify
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Skill, User
from todarith.mod_database.forms import AskForm
from flask_login import current_user, login_required
from todarith.mod_database import moddb
from todarith.mod_database.functions import getDBAnswer
from random import random

from sqlalchemy import func


from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
session = Session()

# Set the route and accepted methods
@moddb.route('/', methods=['GET', 'POST'])
@moddb.route('/<string:getSkills>', methods=['GET'])
def browse(getSkills='1'):
    skillIds = getSkills.split('&')
    skills = []
    for skill in skillIds:
        skills.append(Skill.query.filter_by(id=skill).first())
    print(skills)

    if len(skills)==1:
        allProbs = skills[0].problems
    else:
        allProbs = []
        for skill in skills:
            problems = skill.problems
            for prob in problems:
                #should be an exception somewhere here that stops from searching all problems in math skill
                fits = True
                for skill in skills:
                    if skill not in prob.skills:
                        fits = False

                if (fits==True) and (prob not in allProbs):
                    allProbs.append(prob)

        #allProbs = list(dict.fromkeys(allProbs)) #remove duplicates
    print(allProbs)

    page = request.args.get('page', 1, type=int)
    per_page=50
    problems = paginate(allProbs, page, per_page)
    lastPage= int(len(allProbs)/per_page)
    return render_template("database/browse.html", problems=problems, skills=skills, page=page, lastPage=lastPage)

def paginate(list, page, per_page):
    start = (page-1)*per_page
    end = start+per_page
    problems = list[start:end]
    return problems

@moddb.route('/_get_skill_query', methods=['GET', 'POST'])
def browse_get_skill_query():
    query = request.args.get('query', "", type=str)
    allSkills = Skill.query.filter(Skill.skillName.ilike('%'+query+'%')).all()
    returnSkill = Skill.query.filter(Skill.skillName.ilike('%'+query+'%')).first()
    returnSkills = []
    try:
        for i in range(1,5):
            returnSkills.append(allSkills[i])
    except:
        returnSkills = allSkills
    #return jsonify(problems=[{'problem': problem.question, 'answer': problem.answer,} for problem in problems])
    return jsonify(returnSkill={'name': returnSkill.skillName, 'id': returnSkill.id})
    #return jsonify(returnSkills=[{'id': skill.id, 'name': skill.skillName,} for skill in returnSkills])


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
    return jsonify(problem=nextProblem.question, answer="")

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
