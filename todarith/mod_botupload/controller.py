from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from todarith import db
from todarith.models import Problem, Topic
from todarith.mod_botupload import botupload
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from todarith.models import User, Problem, Topic
from todarithgen import generator
from todarith.mod_botupload.postProc import checkAll, checkTopicExists

@botupload.route('/', methods=['GET', 'POST'])
def generate():
    uploaded_count = 0
    duplicate_count = 0
    uploadedList = []
    duplicateList = []
    list = generator.singleDigitAddition()
    prob=""
    ans=""
    for tup in list:
        if len(tup) == 2:
            prob=tup[0]
            ans=tup[1]
        if (checkAll(prob, ans)==True):
            uploaded_count += 1
            Problem.create(
                question=prob,
                answer=ans,
                topic_id=1,
                poster_id=1,
                confirmedCorrect=None,
                difficultyLevel=None,
                expectedTime=None,
                hasSolution=True
            )
            uploadedList.append(tup)
        else:
            duplicate_count += 1
            duplicateList.append(tup)

    return(render_template("botupload/generated.html", dupList=duplicateList, upList = uploadedList, upCount = uploaded_count, dupCount = duplicate_count))
