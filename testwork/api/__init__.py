from flask import Blueprint

bp = Blueprint('api', __name__)

from testwork.api import cpu