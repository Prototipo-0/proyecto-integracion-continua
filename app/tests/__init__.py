from flask import Blueprint

tests_bp = Blueprint("tests", __name__)

from app.tests import routes