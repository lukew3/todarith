from flask import request, render_template, redirect, url_for, jsonify
from todarith import db
from todarith.models import Problem, Topic, User
from flask_login import current_user, login_required
from todarith.mod_learn import learn
from random import random

# Set the route and accepted methods
@learn.route('/')
def learnHome():
    return(render_template("learn/learnHome.html"))

@learn.route('/practice')
def practice():
    return(render_template("learn/practice.html"))
