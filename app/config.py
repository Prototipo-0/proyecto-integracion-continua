import os


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "clave-temporal-desarrollo"
    )

    DB_HOST = os.getenv("DB_HOST", "db")
    DB_NAME = os.getenv("DB_NAME", "proyecto_db")
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")
    DB_PORT = os.getenv("DB_PORT", "5432")