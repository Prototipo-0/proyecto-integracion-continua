
import pytest

from app import create_app


@pytest.fixture
def app():
    application = create_app()

    application.config.update(
        TESTING=True,
        SECRET_KEY="clave-pruebas",
        ENABLE_DIAGNOSTIC_ENDPOINT=False
    )

    yield application


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def authenticated_client(client):
    with client.session_transaction() as session:
        session["user_id"] = 1
        session["user_name"] = "Usuario de prueba"
        session["user_email"] = "prueba@example.com"
        session["user_role"] = "Administrador"

    return client
