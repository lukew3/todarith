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
from mathgenerator import mathgen
import random

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

@botupload.route('/v2', methods=['GET', 'POST'])
def generate_v2():
    poster = User.query.filter_by().first()
    gen_list = mathgen.getGenList()
    
    # Generates a defined number of problems, random generator id's for each
    for _ in range(100):
        gen_id = random.randint(0, len(gen_list)-1)
        prob, ans = mathgen.genById(gen_id)
        generator_name = gen_list[gen_id][1]
        # If statement makes sure there isnt a duplicate
        if Problem.query.filter_by(question=prob).first() == None: 
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
            # Add the math skill
            thisProb.skills.append(Skill.query.filter_by(id=1).first())
            # If generator_name skill doesn't yet exist, create it and then add it
            if Skill.query.filter_by(skillName=generator_name).first() == None:
                Skill.create(
                    skillName = generator_name
                )
            thisProb.skills.append(Skill.query.filter_by(skillName=generator_name).first())
            # Add generated tag in order to prevent disaster if a bad generator is made
            thisProb.skills.append(Skill.query.filter_by(skillName="generated").first())
            db.session.commit()
    return "<p>Problems added</p>"
