import os
import sys

APP_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "app")
)

sys.path.insert(0, APP_DIR)

from app import app  # noqa: E402


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"DevOps Application is Running!"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"