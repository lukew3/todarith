from flask import Blueprint

botupload = Blueprint('botupload', __name__)

from . import controller
