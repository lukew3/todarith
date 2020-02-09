from flask import request, render_template, redirect, url_for
from todarith import db
from todarith.models import Problem, Classnum, Section, Topic
from todarith.mod_post.forms import QuestionForm, BranchForm
from todarith.mod_post import post

@post.route("/new", methods=['GET', 'POST'])
def newPost():
    form = QuestionForm()
    form.classNumber.choices = [(row.id, row.className) for row in Classnum.query.all()]
    form.section.choices = [(row.id, row.section) for row in Section.query.filter(Section.class_id == 1) ]
    form.topic.choices = [(row.id, row.topic) for row in Topic.query.all()]
    if form.validate_on_submit():
        newQuestion = Problem(question=form.question.data, answer=form.answer.data, classNumber=form.classNumber.data, section=form.section.data, topic=form.topic.data)
        db.session.add(newQuestion)
        db.session.commit()
        return redirect(url_for('main.explore'))
    return render_template('post/newpost.html', form=form)

@post.route('/edit')
def edit():
    return render_template('post/editpost.html')


@post.route('/createClass', methods=['GET', 'POST'])
def createClass():
    form = BranchForm()
    form.parentBranch.choices = [(row.id, row.className) for row in Classnum.query.all()]
    branchtype = 'classnum'
    if form.validate_on_submit():
        newClass = Classnum(className=form.branchName.data)
        db.session.add(newClass)
        db.session.commit()
        return redirect(url_for('post.newPost'))
    return render_template('post/createBranch.html', form=form, branchtype=branchtype)

@post.route('/createSection', methods=['GET', 'POST'])
def createSection():
    form = BranchForm()
    form.parentBranch.choices = [(row.id, row.className) for row in Classnum.query.all()]
    branchtype = 'section'
    if form.validate_on_submit():
        #cvhange class id to number
        newSection = Section(class_id=form.parentBranch.data, className=form.branchName.data)
        db.session.add(newSection)
        db.session.commit()
        return redirect(url_for('post.newPost'))
    return render_template('post/createBranch.html', form=form, branchtype=branchtype)

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
