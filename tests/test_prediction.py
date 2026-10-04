from app import app
import pytest


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


@pytest.mark.parametrize(
    "data, expected_message",
    [
        (
            {"area": "0", "bedrooms": "3", "age": "5"},
            b"Area must be greater than zero."
        ),
        (
            {"area": "1200", "bedrooms": "0", "age": "5"},
            b"Bedrooms must be greater than zero."
        ),
        (
            {"area": "1200", "bedrooms": "3", "age": "-1"},
            b"Age cannot be negative."
        ),
    ]
)
def test_prediction_validation(data, expected_message):
    client = app.test_client()

    with client.session_transaction() as session:
        session["user_id"] = 1

    response = client.post(
        "/predict",
        data=data
    )

    assert response.status_code == 200
    assert expected_message in response.data
