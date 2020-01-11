from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from todarith import db
from flask_login import login_user, current_user, logout_user, login_required
from todarith.models import User
from todarith.mod_auth.forms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__)

# Set the route and accepted methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.explore'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            redirect(url_for('main.explore'))
        else:
            flash('Login Unsuccessful')
    #if form.validate_on_submit():
    #    return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    if form.validate_on_submit():
        return redirect(url_for('main.explore'))

    return render_template('/auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.explore'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('/auth/register.html', form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.explore'))
