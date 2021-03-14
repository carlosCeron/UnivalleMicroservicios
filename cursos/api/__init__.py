from flask import Blueprint

curso_api = Blueprint('api', __name__)

from . import routes
