from flask import Blueprint, request, render_template
from todarith import db
from todarith import mysql
#from todarith.mod_auth.forms import LoginForm
from todarith.models import Problem

main = Blueprint('main', __name__)

# Set the route and accepted methods
@main.route('/')
def landing():
    #conn = mysql.connect()
    #cur = conn.cursor()
    #cur.execute('''CREATE TABLE users (id INTEGER, name VARCHAR(30), email VARCHAR(100), password VARCHAR(100))''')
    return(render_template("main/landing.html"))

@main.route('/explore')
def explore ():
    return(render_template("main/explore.html"))
