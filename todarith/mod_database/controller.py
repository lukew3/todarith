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
from Naked.toolshed.shell import execute_js, muterun_js, run_js #run nodejs scripts
from sqlalchemy import func

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
session = Session()

#functions
def getProb(type, skillId):
    if type=="solve":
        probList = db.session.query(Problem).filter(Problem.skills.any(Skill.id.in_([skillId])), Problem.hasSolution==False).all()
    elif type=="sort":
        probList = db.session.query(Problem).filter_by().all()

    if probList != []:
        randIndex = int(random()*(len(probList)))
        nextProblem = probList[randIndex]
    else:
        return jsonify(id=0, problem="No unsolved problems found for this skill", answer="")

    if type=="solve":
        return jsonify(problem=nextProblem.question, answer="")
    elif type=="sort":
        return jsonify(id=nextProblem.id, problem=nextProblem.question, answer=nextProblem.answer, skills=[{'skillId': skill.id, 'skillName': skill.skillName,} for skill in nextProblem.skills])

def paginate(list, page, per_page):
    start = (page-1)*per_page
    end = start+per_page
    problems = list[start:end]
    return problems

def skillFilter(skills):
    #REPLACE THIS ASAP, the process is slow and inefficient, even with only two skills
    #Accepts a list of skills and returns a list of Problems that include all of the skills in the list
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
    return allProbs

#BROWSE
# Set the route and accepted methods
@moddb.route('/', methods=['GET', 'POST'])
@moddb.route('/<string:getSkills>', methods=['GET'])
def browse(getSkills='Math'):
    skillIds = getSkills.split('&')
    skills = []
    for skill in skillIds:
        skills.append(Skill.query.filter_by(skillName=skill).first())

    if len(skills)==1:
        allProbs = skills[0].problems
    else:
        allProbs = skillFilter(skills)

    page = request.args.get('page', 1, type=int)
    per_page=25
    problems = paginate(allProbs, page, per_page)
    lastPage= int(len(allProbs)/per_page)
    if int(len(allProbs)%per_page) != 0:
        lastPage += 1
    return render_template("database/browse.html", problems=problems, skills=skills, page=page, lastPage=lastPage)

@moddb.route('/_get_skill_query', methods=['GET', 'POST'])
def browse_get_skill_query():
    query = request.args.get('query', "", type=str)
    allSkills = Skill.query.filter(Skill.skillName.ilike('%'+query+'%')).all()
    returnSkill = Skill.query.filter(Skill.skillName.ilike('%'+query+'%')).first()
    returnSkills = []
    if len(allSkills) > 3:
        for i in range(1,3):
            returnSkills.append(allSkills[i])
    else:
        returnSkills=allSkills
    return jsonify(returnSkills=[{'id': skill.id, 'name': skill.skillName,} for skill in returnSkills])

#ASK
@moddb.route('/ask', methods=['GET', 'POST'])
def ask():
    return render_template('database/ask.html')

@moddb.route('/ask/_get_problem_input')
def ask_get_problem_input():
    prob = request.args.get('problem', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = (User.query.filter_by().first()).id
    dbAns = getDBAnswer(prob)
    solution = dbAns
    if dbAns=="unavailable":
        calcAns = attemptSolve(prob)
        if calcAns=="unsolved":
            hasSol=False
        else:
            hasSol=True
        Problem.create(
            question=prob,
            answer=calcAns,
            poster_id=poster,
            correctnessRating=0,
            sortRating=0,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=hasSol
        )
        curProb = Problem.query.filter_by(question=prob).first()
        curProb.skills.append(Skill.query.filter_by(id=1).first())
        db.session.commit()
        solution = calcAns
    return jsonify(answer="The answer is: " + solution)

def attemptSolve(prob):
    response = muterun_js('todarith/static/mathsteps2/index.js', prob)
    print("ERROR: " + str(response.stderr))
    print("RESPONSE WAS: " + str(response.stdout) )
    out = str(response.stdout)
    if out=="b'\\n'":
        return "unsolved"
    else:
        ans = out[2:-3]
        print(ans)
        return ans

@moddb.route('/ask/_add_solved')
def ask_add_solved():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    #cat = request.args.get('category', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = (User.query.filter_by().first()).id
    if db.session.query(Problem).filter_by(question=prob).first() != None:
        pass
    else:
        Problem.create(
            question=prob,
            answer=ans,
            poster_id=poster,
            correctnessRating=0,
            sortRating=0,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=True
        )
        curProb = Problem.query.filter_by(question=prob).first()
        curProb.skills.append(Skill.query.filter_by(id=1).first())
        db.session.commit()
    return jsonify(answer=ans)
#ADD
@moddb.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('database/add.html')

@moddb.route('/add/_get_problem_input')
def add_get_problem_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    #cat = request.args.get('category', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = (User.query.filter_by().first()).id
    if db.session.query(Problem).filter_by(question=prob).first() != None:
        return jsonify(result="Duplicate Found")
    else:
        Problem.create(
            question=prob,
            answer=ans,
            poster_id=poster,
            correctnessRating=0,
            sortRating=0,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=True
        )
        curProb = Problem.query.filter_by(question=prob).first()
        curProb.skills.append(Skill.query.filter_by(id=1).first())
        db.session.commit()
        return jsonify(result="Problem " + prob + " added")


@moddb.route('/answer', methods=['GET', 'POST'])
def answer():
    skills = Skill.query.filter_by().all()
    unsolved = db.session.query(Problem).filter(Problem.skills.any(Skill.id.in_([1])), Problem.hasSolution==False).all()
    if unsolved != []:
        randIndex = int(random()*(len(unsolved)))
        problem = unsolved[randIndex]
    else:
        return render_template('database/noanswer.html')
    return render_template('database/answer.html', problem=problem, skills=skills)

@moddb.route('/answer/_get_answer_input')
def get_answer_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = (User.query.filter_by().first()).id
    currentProblem = db.session.query(Problem).filter_by(question=prob).first()
    currentProblem.update(
        answer = ans,
        hasSolution = True,
        correctnessRating = currentProblem.correctnessRating + 1
    )
    if getProb("solve", 1) == None:
        return render_template('database/noanswer.html')
    else:
        return getProb("solve", 1)

@moddb.route('/answer/_skill_select')
def answer_skill_select():
    skillId = request.args.get('skillId', 1, type=int)
    return getProb("solve", skillId)

@moddb.route('/_flag_problem')
def flag_problem():
    prob = request.args.get('problem', "", type=str)
    currentProblem = db.session.query(Problem).filter_by(question=prob).first()
    currentProblem.update(
        correctnessRating = currentProblem.correctnessRating - 1
    )
    return getProb("Solve", 1)

@moddb.route('/_skip_problem')
def skip_problem():
    return getProb("solve", 1)

#SORT
@moddb.route('/sort')
def sort():
    problem = Problem.query.filter_by(sortRating=0).first()
    return render_template('database/sort.html', problem=problem)

@moddb.route('/sort/_next_problem')
def sort_next_problem():
    return getProb("sort", 1)

@moddb.route('/_add_skill')
def add_skill():
    skillId = request.args.get('skillId', 0, type=int)
    probId = request.args.get('probId', 0, type=int)
    prob = Problem.query.filter_by(id=probId).first()
    prob.sortRating = 1
    skill = Skill.query.filter_by(id=skillId).first()
    prob.skills.append(skill)
    db.session.commit()
    return jsonify(name=skill.skillName, id=skill.id)

@moddb.route('/_create_skill')
def create_skill():
    skillName = request.args.get('skillName', type=str)
    Skill.create(
        skillName=skillName
    )
    skill = Skill.query.filter_by(skillName=skillName).first()
    return jsonify(skillName=skill.skillName, id=skill.id)

@moddb.route('/_remove_skill')
def remove_skill():
    skillId = request.args.get('skillId', 0, type=int)
    probId = request.args.get('probId', 0, type=int)
    prob = Problem.query.filter_by(id=probId).first()
    skill = Skill.query.filter_by(id=skillId).first()

    prob.skills.remove(skill)
    db.session.commit()
    return ""


@moddb.route("/<string:problem_id>")
def viewProblem(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    return render_template('post/problem.html', problem=problem)
