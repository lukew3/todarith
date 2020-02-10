from flask import request, render_template, redirect, url_for
from todarith.database import db
from todarith.models import User, Problem, Topic
from todarith.mod_post.forms import QuestionForm, TopicForm
from todarith.mod_post import post
from flask_wtf import FlaskForm

@post.route("/new", methods=['GET', 'POST'])
def newPost():
    form = QuestionForm()
    form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
    if form.validate_on_submit() == False:
        print("Why")
        print(Problem(question=form.question.data, answer=form.answer.data, ))
    if form.validate_on_submit():
        print('problem added')
        #newQuestion = Problem(question=form.question.data, answer=form.answer.data, topic=form.topic.data)
        newQuestion = Problem(question=form.question.data, answer=form.answer.data, confirmedCorrect=None, difficultyLevel=None, expectedTime=None, otherTags=None)
        db.session.add(newQuestion)
        db.session.commit()
        return redirect(url_for('main.explore'))
    return render_template('post/newpost.html', form=form)

@post.route('/edit')
def edit():
    return render_template('post/editpost.html')

"""
@post.route('/createTopic', methods=['GET', 'POST'])
def createTopic():
    branchtype = 'topic'
    form = BranchForm()
    if form.validate_on_submit():
        newTopic = Topic(parentBranch=form.parentBranch.data, className=form.branchName.data)
        db.session.add(newTopic)
        db.session.commit()
        return redirect(url_for('post.newPost'))
    return render_template('post/createBranch.html', form=form, branchtype=branchtype)
"""
