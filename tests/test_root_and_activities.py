def test_root_redirects_to_static_page(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_structure(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) > 0

    first_activity = next(iter(payload.values()))
    assert {"description", "schedule", "max_participants", "participants"}.issubset(
        first_activity.keys()
    )
    assert isinstance(first_activity["participants"], list)
