import requests

BASE_URL = "http://localhost:8000"


def test_successfully_sign_guest_book():
    data = {"name": "John Doe", "message": "Great service!"}
    response = requests.post(f"{BASE_URL}/sign", data=data)
    assert response.status_code == 200
    assert "Thank you, John Doe, for your message!" in response.text


def test_sign_with_missing_name():
    data = {"message": "Missing name!"}
    response = requests.post(f"{BASE_URL}/sign", data=data)
    assert response.status_code == 400
    assert "missing name" in response.text.lower()


def test_sign_with_missing_message():
    data = {"name": "Jane Doe"}
    response = requests.post(f"{BASE_URL}/sign", data=data)
    assert response.status_code == 400
    assert "missing message" in response.text.lower()
