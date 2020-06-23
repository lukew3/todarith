from flask import Blueprint

moddb = Blueprint('moddb', __name__)

from . import controller
