from unittest.mock import patch, MagicMock


def test_incidents_redirect_without_session(client):
    response = client.get("/incidents/")

    assert response.status_code == 302
    assert "/login" in response.location


@patch("app.incidents.routes.get_db_connection")
def test_incidents_list_authenticated(mock_db, authenticated_client):
    connection = MagicMock()
    cursor = connection.cursor.return_value.__enter__.return_value
    cursor.fetchall.return_value = []

    mock_db.return_value = connection

    response = authenticated_client.get("/incidents/")

    assert response.status_code == 200
    assert b"incidencias" in response.data.lower()


@patch("app.incidents.routes.get_db_connection")
def test_create_incident_empty_fields(mock_db, authenticated_client):
    connection = MagicMock()
    mock_db.return_value = connection

    response = authenticated_client.post(
        "/incidents/create",
        data={
            "titulo": "",
            "descripcion": "",
            "categoria_id": "1",
            "prioridad_id": "1"
        }
    )

    assert response.status_code == 200
    assert connection.commit.call_count == 0