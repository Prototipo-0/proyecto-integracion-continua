from flask import jsonify, request
from app.tests import tests_bp
from app.services.database import get_db_connection


@tests_bp.route("/pruebas", methods=["POST"])
def crear_prueba():
    datos = request.get_json(silent=True) or {}
    descripcion = datos.get("descripcion", "").strip()

    if not descripcion:
        return jsonify({
            "estado": "error",
            "mensaje": "La descripcion es obligatoria"
        }), 400

    if len(descripcion) > 255:
        return jsonify({
            "estado": "error",
            "mensaje": "La descripcion no puede superar 255 caracteres"
        }), 400

    conexion = None

    try:
        conexion = get_db_connection()

        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO pruebas (descripcion)
                VALUES (%s)
                RETURNING id
                """,
                (descripcion,)
            )

            nuevo_id = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT id, descripcion, fecha_creacion
                FROM pruebas
                WHERE id = %s
                """,
                (nuevo_id,)
            )

            registro = cursor.fetchone()

        conexion.commit()

        return jsonify({
            "estado": "correcto",
            "mensaje": "Registro guardado y consultado correctamente",
            "datos": {
                "id": registro[0],
                "descripcion": registro[1],
                "fecha_creacion": registro[2].isoformat()
            }
        }), 201

    except Exception:
        if conexion:
            conexion.rollback()

        return jsonify({
            "estado": "error",
            "mensaje": "No fue posible completar la prueba de base de datos"
        }), 500

    finally:
        if conexion:
            conexion.close()