from unittest.mock import patch


def test_login_page_returns_200(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_login_empty_fields_redirect(client):
    response = client.post(
        "/login",
        data={"correo": "", "password": ""}
    )

    assert response.status_code == 302
    assert "/login" in response.location


@patch("app.auth.routes.get_db_connection")
def test_login_invalid_credentials(mock_db, client):
    mock_db.return_value.cursor.return_value.__enter__.return_value.fetchone.return_value = None

    response = client.post(
        "/login",
        data={
            "correo": "incorrecto@example.com",
            "password": "incorrecta"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"incorrectos" in response.data


def test_authenticated_user_redirected_from_login(authenticated_client):
    response = authenticated_client.get("/login")

    assert response.status_code == 302
    assert "/dashboard/" in response.location


def test_logout_clears_session(authenticated_client):
    response = authenticated_client.get("/logout")

    assert response.status_code == 302

    with authenticated_client.session_transaction() as session:
        assert "user_id" not in session