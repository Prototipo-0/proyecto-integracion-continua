
from functools import wraps

from flask import session, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    return generate_password_hash(password)


def verify_password(password_hash, password):
    return check_password_hash(password_hash, password)


def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        if not session.get("user_id"):
            flash("Debes iniciar sesión para acceder.", "warning")
            return redirect(url_for("auth.login"))

        return function(*args, **kwargs)

    return wrapper


def role_required(*roles_permitidos):
    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            if not session.get("user_id"):
                flash("Debes iniciar sesión.", "warning")
                return redirect(url_for("auth.login"))

            if session.get("user_role") not in roles_permitidos:
                abort(403)

            return function(*args, **kwargs)

        return wrapper

    return decorator
