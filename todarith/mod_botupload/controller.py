from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort, jsonify
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
def botupload_main():
    return(render_template("botupload/botupload.html"))

@botupload.route('/generate_problem')
def generate_problem():
    gen_id = request.args.get('gen_id', -1, type=int)

    poster = User.query.filter_by().first()
    gen_list = mathgen.getGenList()
    prob, ans = mathgen.genById(gen_id)
    generator_name = gen_list[gen_id][1]
    # If statement makes sure there isnt a duplicate
    if Problem.query.filter_by(question=prob).first() == None: 
        mathSkill = Skill.query.filter_by(id=1).first()
        Problem.create(
            question=prob,
            answer=ans,
            poster_id=poster.id,
            correctnessRating=1,
            sortRating=1,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=True,
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
    else:
        return jsonify(problem="Problem already exists", answer="N/A", skill="N/A")
    return jsonify(problem=prob, answer=ans, skill=generator_name)

