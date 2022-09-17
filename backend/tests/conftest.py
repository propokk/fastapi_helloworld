import pytest
from starlette.testclient import TestClient
from backend.main import app
from backend.core.config import settings

auth0_token = settings.AUTH0_TEST_TOKEN

@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def token():
    token = auth0_token
    return token