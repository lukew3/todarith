from todarith.mod_search.forms import ProblemSearchForm
from flask import flash, render_template, request, redirect
from todarith.models import User, Problem, Topic
from todarith.mod_search import search

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

#form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
#results = [(row.id, row.problem) for row in Problem.query.filter_by(problem=search_string)]
