from flask import Blueprint

learn = Blueprint('learn', __name__)

from . import controller
