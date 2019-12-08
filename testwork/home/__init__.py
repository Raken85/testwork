from flask import Blueprint

bp = Blueprint('home', __name__)

from testwork.home import routes