from flask import request, render_template, redirect, url_for, jsonify
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Topic, User
from todarith.mod_database.forms import AskForm
from flask_login import current_user, login_required
from todarith.mod_database import moddb


# Set the route and accepted methods
@moddb.route('/')
def browse():
    return(render_template("database/browse.html"))

@moddb.route('/ask', methods=['GET', 'POST'])
def ask():
    return render_template('database/ask.html')


@moddb.route('/_get_problem_input')
def get_problem_input():
    #print("Somethings")
    prob = request.args.get('problem', "", type=str)
    ans = request.args.get('answer', "", type=str)
    cat = request.args.get('category', "", type=str)
    print("Problem:" + prob)
    print("Answer:" + ans)
    print("Category:" + cat)

    #solved = checkSolved(ans)
    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1
    #form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]

    return jsonify(result="Problem \"" + prob + "=" + ans + "\" was not added")
