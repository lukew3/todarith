from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Topic
from todarith.mod_main import main


# Set the route and accepted methods
@main.route('/')
def landing():
    return(render_template("main/landing.html"))

@main.route('/explore')
def explore():
    problems = Problem.query.all()
    return render_template('main/explore.html', problems=problems)
"""
@main.route('/topicBrowser')
def topicBrowser():
    topics = Topic.query.all()
    return render_template('main/topicBrowser.html', topics=topics)
"""
@main.route('/topicBrowser/<int:topic_id>')
def topicBrowser(topic_id):
    currentTopic = Topic.query.filter_by(id=topic_id).first()
    subtopics = Topic.query.filter_by(parentTopic_id=topic_id)
    lastID=currentTopic.parentTopic_id
    if lastID==None:
        lastID = 1
    print(lastID)
    return render_template('main/topicBrowser.html', currentTopic=currentTopic, subtopics=subtopics, lastID=lastID)

@main.route('/sitemap')
def siteMap():
    return render_template('main/sitemap.html')
