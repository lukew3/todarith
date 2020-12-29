from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort, jsonify
)
from todarith import db
from todarith.models import Problem, Skill, User
from todarith.mod_botupload import botupload
from werkzeug.utils import secure_filename
from todarith.models import User, Problem, Skill
from mathgenerator import mathgen
import random
import time

@botupload.route('/', methods=['GET', 'POST'])
def botupload_main():
    return(render_template("botupload/botupload.html"))

@botupload.route('/request_generate_problem')
def request_generate_problem():
    gen_id = request.args.get('gen_id', -1, type=int)
    problem, answer, skill = generate_problem(gen_id)
    return jsonify(problem=problem, answer=answer, skill=skill)

def generate_problem(gen_id):
    poster = User.query.filter_by().first()
    gen_list = mathgen.getGenList()
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
        return prob, ans, generator_name
    else:
        return "Problem already exists", "N/A", "N/A"

@botupload.route('/start')
def start_background():
    # executor.submit(background_generation)
    return "<h3>Generation started</h3>"

@botupload.route('/stop')
def stop_background():
    return "<h3>Generation stopped</h3>"

def background_generation():
    pigs_fly = False
    while pigs_fly == False:
        gen_id = random.randint()
        p, a, s = generate_problem(gen_id)
        print(p)
        time.sleep(1)
