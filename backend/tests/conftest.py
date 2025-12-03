import pytest
import json
import datetime
import jwt
from httpx import Client, WSGITransport
from app.create_app import create_minimal_app


@pytest.fixture(scope="session")
def app():
    return create_minimal_app()

@pytest.fixture(scope="session")
def http_client(app):
    with Client(
        transport=WSGITransport(app=app), 
        base_url="http://127.0.0.1:8000",
    ) as client:
        yield client

@pytest.fixture(scope="session")
def token():
    payload = {
        "user": json.dumps({"id": 1}),
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60)
    }

    token = jwt.encode(payload, "Techsolutio@2025##")
    yield token


#pytest tests -v --cov=app