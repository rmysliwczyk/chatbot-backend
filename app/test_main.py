import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from .main import app

load_dotenv()

client = TestClient(app)


def test_auth_token_returns_405_not_allowed_for_get():
    # This endpoint doesn't allow GET, we expect 405 Method Not Allowed
    response = client.get("/auth/token")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_auth_token_returns_200_and_valid_token_for_post():
    username = os.getenv("DEFAULT_ADMIN_LOGIN")
    password = os.getenv("DEFAULT_ADMIN_PASSWORD")
    print(username, password)
    response = client.post(
        "/auth/token", data={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
