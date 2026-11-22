def test_dashboard_redirects_without_session(client):
    response = client.get("/dashboard/")

    assert response.status_code == 302
    assert "/login" in response.location


def test_dashboard_access_with_session(authenticated_client):
    response = authenticated_client.get("/dashboard/")

    assert response.status_code == 200


def test_dashboard_displays_user(authenticated_client):
    response = authenticated_client.get("/dashboard/")

    assert response.status_code == 200
    assert b"Usuario de prueba" in response.data