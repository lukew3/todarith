from flask import Blueprint, request, render_template
from todarith import db
#from todarith.mod_auth.forms import LoginForm
from todarith.mod_main.models import Problem

main = Blueprint('main', __name__)

# Set the route and accepted methods
@main.route('/')
def landing():
    return(render_template("main/landing.html"))
