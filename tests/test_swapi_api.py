import requests
import pytest
import json



def test_status_code():
    """Verify that the status code is 200."""
    response = requests.get("https://swapi.dev/api/people/1/")
    assert response.status_code == 200

def test_verify_name_of_star_11():
    """Verify that the name of star 11 is Geonosis."""
    response = requests.get("https://swapi.dev/api/planets/11/")

    data = response.json()
    assert data["name"] == "Geonosis"
    print("\n\n **** Test passed ****\n")


def test_create_new_post():
    """Verify that the new post is created successfully."""
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