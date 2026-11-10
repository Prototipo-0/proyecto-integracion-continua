
from flask import (
    render_template,
    session,
    flash,
    redirect,
    url_for,
    request
)

from psycopg2.extras import RealDictCursor

from app.incidents import incidents_bp
from app.services.database import get_db_connection
from app.services.security import login_required


@incidents_bp.route("/")
@login_required
def index():

    connection = None

    try:
        connection = get_db_connection()

        with connection.cursor(cursor_factory=RealDictCursor) as cursor:

            rol = session.get("user_role")
            usuario_id = session.get("user_id")

            consulta = """
                SELECT
                    i.id,
                    i.titulo,
                    i.descripcion,
                    i.fecha_creacion,
                    solicitante.nombre AS solicitante,
                    tecnico.nombre AS tecnico,
                    c.nombre AS categoria,
                    p.nombre AS prioridad,
                    e.nombre AS estado
                FROM incidencias i
                INNER JOIN usuarios solicitante
                    ON i.solicitante_id = solicitante.id
                LEFT JOIN usuarios tecnico
                    ON i.tecnico_id = tecnico.id
                INNER JOIN categorias c
                    ON i.categoria_id = c.id
                INNER JOIN prioridades p
                    ON i.prioridad_id = p.id
                INNER JOIN estados e
                    ON i.estado_id = e.id
            """

            if rol == "Solicitante":
                cursor.execute(
                    consulta + """
                    WHERE i.solicitante_id = %s
                    ORDER BY i.fecha_creacion DESC
                    """,
                    (usuario_id,)
                )

            elif rol in ("Administrador", "Tecnico"):
                cursor.execute(
                    consulta + " ORDER BY i.fecha_creacion DESC"
                )

            else:
                flash("No tienes permisos para consultar incidencias.", "danger")
                return render_template(
                    "incidents/list.html",
                    incidencias=[],
                    usuario=session.get("user_name"),
                    rol=rol
                )

            incidencias = cursor.fetchall()

        return render_template(
            "incidents/list.html",
            incidencias=incidencias,
            usuario=session.get("user_name"),
            rol=rol
        )

    except Exception:
        flash("No fue posible consultar las incidencias.", "danger")
        return render_template(
            "incidents/list.html",
            incidencias=[],
            usuario=session.get("user_name"),
            rol=session.get("user_role")
        )

    finally:
        if connection:
            connection.close()


@incidents_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():

    connection = None

    try:
        connection = get_db_connection()

        with connection.cursor(cursor_factory=RealDictCursor) as cursor:

            if request.method == "POST":

                titulo = request.form.get("titulo", "").strip()
                descripcion = request.form.get("descripcion", "").strip()
                categoria_id = request.form.get("categoria_id", "")
                prioridad_id = request.form.get("prioridad_id", "")

                if not titulo or not descripcion:
                    flash("El título y la descripción son obligatorios.", "warning")

                elif len(titulo) > 200:
                    flash("El título no puede superar los 200 caracteres.", "warning")

                else:
                    try:
                        categoria_id = int(categoria_id)
                        prioridad_id = int(prioridad_id)
                    except (ValueError, TypeError):
                        flash("Selecciona una categoría y prioridad válidas.", "warning")
                    else:
                        cursor.execute(
                            "SELECT id FROM categorias WHERE id = %s AND activo = TRUE",
                            (categoria_id,)
                        )
                        categoria = cursor.fetchone()

                        cursor.execute(
                            "SELECT id FROM prioridades WHERE id = %s",
                            (prioridad_id,)
                        )
                        prioridad = cursor.fetchone()

                        cursor.execute(
                            "SELECT id FROM estados WHERE nombre = %s",
                            ("Abierta",)
                        )
                        estado = cursor.fetchone()

                        if not categoria or not prioridad or not estado:
                            flash("Los datos seleccionados no son válidos.", "warning")

                        else:
                            cursor.execute(
                                """
                                INSERT INTO incidencias (
                                    titulo,
                                    descripcion,
                                    solicitante_id,
                                    categoria_id,
                                    prioridad_id,
                                    estado_id
                                )
                                VALUES (%s, %s, %s, %s, %s, %s)
                                RETURNING id
                                """,
                                (
                                    titulo,
                                    descripcion,
                                    session["user_id"],
                                    categoria_id,
                                    prioridad_id,
                                    estado["id"]
                                )
                            )

                            incidencia_id = cursor.fetchone()["id"]

                            cursor.execute(
                                """
                                INSERT INTO historial_incidencias (
                                    incidencia_id,
                                    usuario_id,
                                    accion,
                                    detalle
                                )
                                VALUES (%s, %s, %s, %s)
                                """,
                                (
                                    incidencia_id,
                                    session["user_id"],
                                    "Creación",
                                    "Incidencia registrada en el sistema."
                                )
                            )

                            connection.commit()

                            flash(
                                f"Incidencia #{incidencia_id} creada correctamente.",
                                "success"
                            )

                            return redirect(url_for("incidents.index"))

            cursor.execute(
                "SELECT id, nombre FROM categorias WHERE activo = TRUE ORDER BY nombre"
            )
            categorias = cursor.fetchall()

            cursor.execute(
                "SELECT id, nombre FROM prioridades ORDER BY nivel DESC"
            )
            prioridades = cursor.fetchall()

        return render_template(
            "incidents/create.html",
            categorias=categorias,
            prioridades=prioridades
        )

    except Exception:
        if connection:
            connection.rollback()

        flash("No fue posible procesar la incidencia.", "danger")

        return redirect(url_for("incidents.index"))

    finally:
        if connection:
            connection.close()
