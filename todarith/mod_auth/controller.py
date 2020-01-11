from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.mod_auth.models import User

auth = Blueprint('auth', __name__)

# Set the route and accepted methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return(render_template("/auth/login.html"))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return(render_template("/auth/register.html"))
