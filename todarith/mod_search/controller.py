from todarith.mod_search.forms import ProblemSearchForm
from flask import flash, render_template, request, redirect, url_for
from todarith.models import User, Problem, Topic
from todarith.mod_search import search
from todarith import db
"""
searchString = ""
@search.route('/', methods=['GET', 'POST'])
def index():
    form = ProblemSearchForm()
    if request.method == 'POST':
        searchString = form.searchQuery.data
        print(searchString)
        return search_results(searchString)
    return render_template('search/search.html', form=form)

@search.route('/results')
def search_results(search):
    #results = []
    search_string = searchString
    results = Problem.query.filter_by(question=search_string)
    return render_template('search/results.html', results=results)
"""
#form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
#results = [(row.id, row.problem) for row in Problem.query.filter_by(problem=search_string)]

@search.route('/', methods=['GET', 'POST'])
def search_page():
    form = ProblemSearchForm()
    if request.method == 'POST':
        if form.validate():
            print("Validation successs")
            searchQuery=form.searchQuery.data
            print(searchQuery)
            #results=Problem.filter_by(question=searchquery).all()
            results = db.session.query(Problem).filter_by(question=searchQuery).all()
            print(results)
            return render_template('search/results.html', searchQuery=searchQuery, results=results)
        else:
            print("Validation failed")
            searchQuery=form.searchQuery.data
            print(searchQuery)
            results = db.session.query(Problem).filter_by(question=searchQuery).all()
            print(results)
            return render_template('search/results.html', searchQuery=searchQuery, results=results)

      #return redirect(url_for('search.search_results', query=query))
    return render_template('search/search.html', form=form)

@search.route('/search_results/<query>')
def search_results(query):
  results = Problem.query.filter_by(problem=query).all()
  return render_template('search/results.html', query=query, results=results)
