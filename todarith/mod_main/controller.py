from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort, jsonify
)
#from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem, Skill, User
from todarith.mod_main import main
from mathgenerator import mathgen

# Set the route and accepted methods
@main.route('/')
def landing():
    problem_count = db.session.query(Problem).count()
    return(render_template("main/landing.html", problemCount=problem_count))

@main.route('/about')
def about():
    return(render_template("main/about.html"))

@main.route('/explore')
def explore():
    #page = request.args.get('page', 1, type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    #return render_template('home.html', posts=posts)

    page = request.args.get('page', 1, type=int)
    problems = Problem.query.paginate(page=page, per_page=50)
    #problems = Problem.query.all()
    return render_template('main/explore.html', problems=problems)

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
    #prob=Problem.query.filter_by(id=2300).first()
    #print(prob.skills)
    return render_template('main/sitemap.html')

@main.route('/topic/<int:topicId>')
def viewTopic(topicId):
    page = request.args.get('page', 1, type=int)
    problems = Problem.query.filter_by(topic_id=topicId).paginate(page=page, per_page=50)
    topic = Topic.query.filter_by(id=topicId).first()
    return render_template('main/viewTopic.html', topic=topic, problems=problems)

@main.route('/user/<string:userId>')
def viewUser(userId):
    page = request.args.get('page', 1, type=int)
    problems = Problem.query.filter_by(poster_id=userId).paginate(page=page, per_page=50)
    username = (User.query.filter_by(id=userId).first()).username
    thisUserId = (User.query.filter_by(id=userId).first()).id
    return render_template('main/viewUser.html', problems=problems, username=username, thisUserId=thisUserId)

@main.route('/solveProblems/<int:topicId>')
def solveProblems(topicId):
    page = request.args.get('page', 1, type=int)
    problems = Problem.query.filter_by(topic_id=topicId, hasSolution=False).paginate(page=page, per_page=50)
    topic = Topic.query.filter_by(id=topicId).first()
    return render_template('main/solveProblems.html', topic=topic, problems=problems)

@main.route('/quizmaker')
def quizMaker():
    return render_template('main/quizMaker.html')

@main.route('/generate/')
@main.route('/generate/<int:genId>')
def generate(genId=0):
    return redirect("https://lukew3.com/mathgenerator")
    generators = mathgen.getGenList()
    genTitle = generators[genId][1]
    output = mathgen.genById(genId)
    return render_template('main/generate.html', genTitle=genTitle, genId=genId, generators=generators, problem=output[0], solution=output[1])

@main.route('/generate/request')
def requestGen():
    genId = request.args.get('genId', 1, type=int)
    generators = mathgen.getGenList()
    genTitle = generators[genId][1]
    output = mathgen.genById(genId)
    return jsonify(problem=output[0], solution=output[1])
