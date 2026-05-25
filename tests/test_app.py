import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Task Tracker" in response.data


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_add_task(client):
    """Test adding a new task."""
    response = client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" in response.data


def test_add_empty_task(client):
    """Test that empty tasks are not added."""
    response = client.post("/add", data={"task": ""}, follow_redirects=True)
    assert response.status_code == 200


def test_complete_task(client):
    """Test marking a task as complete."""
    client.post("/add", data={"task": "Complete Me"}, follow_redirects=True)
    response = client.get("/complete/1", follow_redirects=True)
    assert response.status_code == 200


def test_delete_task(client):
    """Test deleting a task."""
    client.post("/add", data={"task": "Delete Me"}, follow_redirects=True)
    response = client.get("/delete/1", follow_redirects=True)
    assert response.status_code == 200
