from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Topic, User
from todarith.mod_database.forms import AskForm
from todarith.mod_database import moddb


# Set the route and accepted methods
@moddb.route('/')
def browse():
    return(render_template("database/browse.html"))

@moddb.route('/ask')
def ask():
    form = AskForm()
    if form.validate_on_submit():
        redirect(url_for('database/'))
    return render_template("database/ask.html", form=form)

"""

@post.route('/_get_problem_input')
def get_problem_input():
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    print("Problem:" + prob)
    print("Answer:" + ans)

    solved = checkSolved(ans)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    #form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
    if checkOriginal(prob, ans):
        Problem.create(
            question=prob,
            answer=ans,
            topic_id=1,
            poster_id=poster,
            confirmedCorrect=None,
            difficultyLevel=None,
            expectedTime=None,
            hasSolution=solved
        )
        return jsonify(result="Problem \"" + prob + "=" + ans + "\" added")
    else:
        return jsonify(result="Problem \"" + prob + "=" + ans + "\" was not added")
"""
