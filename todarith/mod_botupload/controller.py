from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from todarith import db
from todarith.models import Problem, Topic
from todarith.mod_botupload import botupload
from flask_wtf import FlaskForm
from todarith.mod_botupload.forms import FileUploadForm
from werkzeug.utils import secure_filename
from todarithgen import generator

@botupload.route('/', methods=['GET', 'POST'])
def generate():
    list = generator.singleDigitAddition()
    return(render_template("botupload/generated.html", list=list))
