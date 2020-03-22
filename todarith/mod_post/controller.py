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

    if current_user.is_authenticated:
        poster = current_user.id
    else:
        poster = 1

    form = QuestionForm()
    form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]

    if request.method == 'POST':
        print(form.answer.data)
        print(form.topic.data)
        prob = form.question.data
        ans = form.answer.data
        solved = checkSolved(ans)
        if (solved==False or checkAll(prob, ans)==True):
            if form.validate():
                print('Validate: True')
                #print(Problem(question=form.question.data, answer=form.answer.data, topic=form.topic.data))
                Problem.create(
                    question=prob,
                    answer=ans,
                    topic_id=form.topic.data,
                    poster_id=poster,
                    confirmedCorrect=None,
                    difficultyLevel=None,
                    expectedTime=None,
                    hasSolution=solved
                )
            else:
                print(form.errors)
                Problem.create(
                    question=prob,
                    answer=ans,
                    topic_id=form.topic.data,
                    poster_id=poster,
                    confirmedCorrect=None,
                    difficultyLevel=None,
                    expectedTime=None,
                    hasSolution=solved
                )
            return redirect(url_for('main.explore'))
        else:
            return ('<h1>Incorrect Problem Solution set</h1>')
    return render_template('post/newpost.html', form=form)

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
