from flask import Blueprint

profesores_api = Blueprint('api', __name__)

from . import routes