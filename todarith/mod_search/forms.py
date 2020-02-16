from wtforms import Form, StringField, SelectField

class ProbelmSearchForm(Form):
    search = StringField('Search for:')
    submit = SubmitField('Search')
