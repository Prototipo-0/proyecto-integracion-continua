from flask import Blueprint

incidents_bp = Blueprint("incidents", __name__)

from app.incidents import routes