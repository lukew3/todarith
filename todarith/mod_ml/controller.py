from flask import request, render_template, redirect, url_for, jsonify
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Skill, User
from flask_login import current_user, login_required
from random import random
from Naked.toolshed.shell import execute_js, muterun_js, run_js #run nodejs scripts
from sqlalchemy import func
from todarith.mod_ml import modml
from todarith.mod_ml.aiSort import createModel, aiSort

@modml.route('/', methods=['GET', 'POST'])
def mlLanding():
    pass

@modml.route('/prepSort')
def prepSort():
    probs = Problem.query.filter_by().all()
    probsCont = []
    probsSkill = []
    for prob in probs:
        print(prob.question)
        print(prob.id)
        print(prob.question + " " + str(prob.skills[1].id))
        probsCont.append(prob.question)
        probsSkill.append(str(prob.skills[1].id))
    questions = " ".join(probsCont)
    skills = " ".join(probsSkill)
    print(questions)
    print(skills)

    with open('todarith/mod_ml/trainingData.txt', 'w') as filehandle:
        for i in range(len(probsCont)):
            filehandle.write('%s\n' % probsCont[i])
            filehandle.write('%s\n' % probsSkill[i])

    return render_template('main/sitemap.html')


@modml.route('/makeModel')
def makeModel():
    questions= []
    skills = []

    with open('todarith/mod_ml/trainingData.txt', 'r') as filehandle:
        skillLine = False
        for line in filehandle:
            currentPlace = line[:-1]
            if skillLine == True:
                skills.append(currentPlace)
            else:
                questions.append(currentPlace)
            skillLine = not skillLine

    createModel(questions, skills)
    return render_template('main/sitemap.html')

@modml.route('/aisort')
def aisort():
    input = '202+7'
    output = int(aiSort(input))
    outputSkill = Skill.query.filter_by(id=output).first()

    print("Skill for {} was {}".format(input, outputSkill.skillName))
    return render_template('main/sitemap.html')
