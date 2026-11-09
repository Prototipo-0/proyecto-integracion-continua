
from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "proyecto_db"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "admin123"),
        port=os.getenv("DB_PORT", "5432")
    )

@app.route("/")
def home():
    return jsonify({
        "mensaje": "Aplicacion de Integracion Continua",
        "estado": "Funcionando"
    })

@app.route("/health")
def health():
    try:
        connection = get_db_connection()
        connection.close()

        return jsonify({
            "aplicacion": "OK",
            "base_de_datos": "Conectada"
        }), 200

    except Exception as error:
        return jsonify({
            "aplicacion": "OK",
            "base_de_datos": "Error",
            "detalle": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
