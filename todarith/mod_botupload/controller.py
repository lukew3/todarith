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
from todarith.mod_botupload.postProc import checkAll, checkTopicExists

@botupload.route('/', methods=['GET', 'POST'])
def generate():
    uploaded_count = 0
    duplicate_count = 0
    uploadedList = []
    duplicateList = []
    list = generator.main()
    prob=""
    ans=""
    for tup in list:
        if len(tup) == 2:
            prob=tup[0]
            ans=tup[1]
        if (checkAll(prob, ans)==True):
            uploaded_count += 1
            myskill=Skill.query.filter_by(id=1).first()
            Problem.create(
                question=prob,
                answer=ans,
                poster_id=1,
                correctnessRating=1,
                difficultyLevel=None,
                expectedTime=None,
                hasSolution=True
            )
            thisProb = Problem.query.filter_by(question=prob).first()
            thisProb.skills.append(myskill)
            uploadedList.append(tup)
            db.session.commit()
        else:
            duplicate_count += 1
            duplicateList.append(tup)

    return(render_template("botupload/generated.html", dupList=duplicateList, upList = uploadedList, upCount = uploaded_count, dupCount = duplicate_count))
