#same thing as routes

from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    return(render_template("auth/signin.html"))
