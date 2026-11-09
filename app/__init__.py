from flask import Flask
from app.config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from app.auth import auth_bp
    from app.dashboard import dashboard_bp
    from app.incidents import incidents_bp
    from app.users import users_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(
        dashboard_bp,
        url_prefix="/dashboard"
    )
    app.register_blueprint(
        incidents_bp,
        url_prefix="/incidents"
    )
    app.register_blueprint(
        users_bp,
        url_prefix="/users"
    )

    return app