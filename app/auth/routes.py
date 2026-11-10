
from flask import (
    request,
    render_template,
    redirect,
    url_for,
    flash,
    session
)

from app.auth import auth_bp
from app.services.database import get_db_connection
from app.services.security import verify_password


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # Si ya existe una sesión, ir al dashboard
    if session.get("user_id"):
        return redirect(url_for("dashboard.index"))

    if request.method == "POST":

        correo = request.form.get("correo", "").strip().lower()
        password = request.form.get("password", "")

        if not correo or not password:
            flash("Ingresa el correo y la contraseña.", "warning")
            return redirect(url_for("auth.login"))

        connection = None

        try:
            connection = get_db_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        u.id,
                        u.nombre,
                        u.correo,
                        u.password_hash,
                        r.nombre AS rol
                    FROM usuarios u
                    INNER JOIN roles r ON u.rol_id = r.id
                    WHERE u.correo = %s
                    AND u.activo = TRUE;
                    """,
                    (correo,)
                )

                usuario = cursor.fetchone()

            if usuario and verify_password(usuario[3], password):

                session.clear()

                session["user_id"] = usuario[0]
                session["user_name"] = usuario[1]
                session["user_email"] = usuario[2]
                session["user_role"] = usuario[4]

                flash("Bienvenido al IT Service Desk.", "success")

                return redirect(url_for("dashboard.index"))

            flash("Correo o contraseña incorrectos.", "danger")

        except Exception:
            flash("No fue posible iniciar sesión. Intenta nuevamente.", "danger")

        finally:
            if connection:
                connection.close()

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Sesión cerrada correctamente.", "info")

    return redirect(url_for("auth.login"))
