from flask import request, render_template, redirect, url_for
from todarith.database import db
from todarith.models import User, Problem, Topic
from todarith.mod_post.forms import QuestionForm, TopicForm
from todarith.mod_post import post
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from todarith.mod_post.postProc import checkAll, checkTopicExists, checkSolved

@post.route("/new", methods=['GET', 'POST'])
def newPost():

    if request.method == 'POST':
        prob_var = request.form.get('problem2')
        print(prob_var)
        return redirect(url_for('post.newPost'))
    return render_template('post/newpost.html')

@post.route('/edit')
def edit():
    return render_template('post/editpost.html')

@post.route('/createTopic', methods=['GET', 'POST'])
def createTopic():
    form = TopicForm()
    form.parentTopic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
    if request.method == 'POST':
        topicName = form.topicName.data
        if form.parentTopic.data == None:
            parentID = 1
        else:
            parentID = form.parentTopic.data

        if checkTopicExists(topicName)==True:
            if form.validate():
                print('Validate: True')
                Topic.create(
                    topicName=topicName,
                    parentTopic_id = parentID
                )
            else:
                print(form.errors)
                Topic.create(
                    topicName=topicName,
                    parentTopic_id = parentID
                )
            return redirect(url_for('main.explore'))
        else:
            return ('<h1>Topic already exists</h1>')
    return render_template('post/newTopic.html', form=form)


@post.route("/<int:problem_id>")
def viewProblem(problem_id):
    problem = Problem.query.get_or_404(problem_id)
    return render_template('post/problem.html', problem=problem)
