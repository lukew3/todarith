from forms import ProblemSearchForm
from flask import flash, render_template, request, redirect
from todarith.models import User, Problem, Topic


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('search.html', form=form)

@app.route('/results')
def search_results(search):
    #results = []
    search_string = search.data['search']
    results = [(row.id, row.problem) for row in Problem.query.filter_by(problem=search_string)]
    return render_template('search/results.html', results=results)

#form.topic.choices = [(row.id, row.topicName) for row in Topic.query.all()]
results = [(row.id, row.problem) for row in Problem.query.filter_by(problem=search_string)]
