
import os
from pathlib import Path
from getpass import getpass

import psycopg2
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash


# Cargar variables del archivo .env
ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")


def create_admin():
    print("\n=== CREAR ADMINISTRADOR IT SERVICE DESK ===\n")

    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electrónico: ").strip().lower()
    password = getpass("Contraseña: ")
    confirmacion = getpass("Confirmar contraseña: ")

    if not nombre or not correo or not password:
        print("ERROR: Todos los campos son obligatorios.")
        return

    if password != confirmacion:
        print("ERROR: Las contraseñas no coinciden.")
        return

    if len(password) < 12:
        print("ERROR: Utiliza al menos 12 caracteres.")
        return

    password_hash = generate_password_hash(password)

    connection = None

    try:
        connection = psycopg2.connect(
            host="localhost",
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        with connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT id FROM roles WHERE nombre = %s",
                    ("Administrador",)
                )

                role = cursor.fetchone()

                if not role:
                    print("ERROR: No existe el rol Administrador.")
                    return

                cursor.execute(
                    """
                    INSERT INTO usuarios
                    (nombre, correo, password_hash, rol_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    (nombre, correo, password_hash, role[0])
                )

                user_id = cursor.fetchone()[0]

        print("\nADMINISTRADOR CREADO CORRECTAMENTE")
        print(f"ID: {user_id}")
        print(f"Nombre: {nombre}")
        print(f"Correo: {correo}")

    except psycopg2.errors.UniqueViolation:
        print("ERROR: Ese correo ya está registrado.")

    except Exception as error:
        print(f"ERROR: {error}")

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    create_admin()
