from flask import Blueprint, request, render_template
from todarith import db

post = Blueprint('post', __name__)

@post.route('/new')
def newPost():
    return render_template('post/newpost.html')

@post.route('/edit')
def edit():
    return render_template('post/editpost.html')
