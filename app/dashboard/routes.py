
from flask import render_template, session

from app.dashboard import dashboard_bp
from app.services.security import login_required


@dashboard_bp.route("/")
@login_required
def index():
    return render_template(
        "dashboard/index.html",
        usuario=session.get("user_name"),
        rol=session.get("user_role")
    )
