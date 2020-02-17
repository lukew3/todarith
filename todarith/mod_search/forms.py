from wtforms import Form, StringField, SelectField, SubmitField

class ProblemSearchForm(Form):
    searchQuery = StringField('Search for:')
    submit = SubmitField('Search')
