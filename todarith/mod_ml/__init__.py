from flask import Blueprint

modml = Blueprint('modml', __name__)

from . import controller
