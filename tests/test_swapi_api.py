import requests
import pytest
import json

@pytest.mark.api
@pytest.mark.sanity
def test_status_code():
    """Verify that the status code is 200."""
    response = requests.get("https://swapi.dev/api/people/1/")
    assert response.status_code == 200

@pytest.mark.api
def test_verify_name_of_star_11():
    """Verify that the name of star 11 is Geonosis."""
    response = requests.get("https://swapi.dev/api/planets/11/")
    data = response.json()
    assert data["name"] == "Geonosis"
    print("\n\n **** Test passed ****\n")

@pytest.mark.api
def test_verify_people_2():
    """Verify that the name of people 2 is C-3P0."""
    response = requests.get("https://swapi.dev/api/people/2/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "C-3PO"
    assert data["height"] == "167"
    assert data["skin_color"] == "gold"
    print("\n\n **** Test passed ****\n")

@pytest.mark.api
def test_create_new_post():
    """Verify that the new post is created successfully. This is a demonstration of a POST request to a test API."""
    # 1. The endpoint that accepts POST requests
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. The data we want to send (the payload)
    payload = {
        "title": "Teaching Playwright",
        "body": "Adding API testing to our syllabus",
        "userId": 101
    }

    # 3. Perform the POST request
    # Using the 'json=' parameter automatically sets the header to 'application/json'
    response = requests.post(url, json=payload)

    # 4. Assertions
    # Status code 201 usually means a resource was successfully "Created"
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data  # The server typically returns the ID of the new item
