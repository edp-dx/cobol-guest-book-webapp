import requests

BASE_URL = "http://localhost:8000"


def test_view_all_guest_book_entries():
    response = requests.get(f"{BASE_URL}/view")
    assert response.status_code == 200
    # Assuming the test database is pre-populated
    assert "John Doe" in response.text  # Check for a known entry


def test_view_guest_book_when_empty():
    # This test assumes you have a way to clear or reset the guest book for testing purposes
    # If not, you might need to manually ensure the guest book is empty or mock the behavior
    response = requests.get(f"{BASE_URL}/view")
    assert response.status_code == 200
    assert (
        "the guest book is empty" in response.text.lower()
    )  # Assuming this is the response for an empty guest book
