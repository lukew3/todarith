from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from todarith import db
from todarith.models import Problem, Skill, User
from todarith.mod_botupload import botupload
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from todarith.models import User, Problem, Skill
from todarithgen import generator
from todarith.mod_botupload.generator import runGenerator
#from todarith.mod_botupload.postProc import checkAll, checkTopicExists

@botupload.route('/', methods=['GET', 'POST'])
def generate():
    uploaded_count = 0
    duplicate_count = 0
    uploadedList = []
    duplicateList = []
    #list = generator.main()
    list = runGenerator()
    prob=""
    ans=""
    for tup in list:
        if len(tup) == 3:
            prob=tup[0]
            ans=tup[1]
            skill=tup[2]
        print(Problem.query.filter_by(question=prob).first())
        poster = User.query.filter_by().first()
        if Problem.query.filter_by(question=prob).first() == None: #makes sure there isnt a duplicate
            uploaded_count += 1
            Problem.create(
                question=prob,
                answer=ans,
                poster_id=poster.id,
                correctnessRating=1,
                sortRating=1,
                difficultyLevel=None,
                expectedTime=None,
                hasSolution=True
            )
            thisProb = Problem.query.filter_by(question=prob).first()
            thisProb.skills.append(Skill.query.filter_by(id=1).first())
            thisProb.skills.append(Skill.query.filter_by(id=skill).first())
            uploadedList.append(tup)
            db.session.commit()
        else:
            duplicate_count += 1
            duplicateList.append(tup)

    return(render_template("botupload/generated.html", dupList=duplicateList, upList = uploadedList, upCount = uploaded_count, dupCount = duplicate_count))
