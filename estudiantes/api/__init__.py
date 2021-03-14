from flask import Blueprint

estudiantes_api = Blueprint('api', __name__)

from . import routes