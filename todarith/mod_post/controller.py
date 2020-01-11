from flask import Blueprint, request, render_template, redirect, url_for
from todarith import db
from todarith.models import Problem, Classnum, Section, Topic
from todarith.mod_post.forms import QuestionForm

post = Blueprint('post', __name__)

@post.route("/new", methods=['GET', 'POST'])
def newPost():
    form = QuestionForm()
    form.classNumber.choices = [(row.id, row.className) for row in Classnum.query.all()]
    form.section.choices = [(row.id, row.section) for row in Section.query.all()]
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
