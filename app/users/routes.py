
from flask import session, abort

from app.users import users_bp
from app.services.security import login_required, role_required


@users_bp.route("/")
@login_required
@role_required("Administrador")
def index():
    return (
        f"Modulo de gestion de usuarios | "
        f"Administrador: {session.get('user_name')}"
    )
