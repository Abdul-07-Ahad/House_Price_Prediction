from app import app


def test_prediction(monkeypatch):
    client = app.test_client()

    monkeypatch.setattr(
        "app.save_prediction",
        lambda *args: None
    )

    monkeypatch.setattr(
        "app.model.predict",
        lambda data: [5000000]
    )

    with client.session_transaction() as session:
        session["user_id"] = 1

    response = client.post(
        "/predict",
        data={
            "area": "1200",
            "bedrooms": "3",
            "age": "5"
        }
    )

    assert response.status_code == 200
    assert b"5,000,000.00" in response.data
