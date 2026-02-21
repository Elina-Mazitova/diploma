import os

import pytest
from dotenv import load_dotenv

from api.dummyjson.clients.auth_client import AuthClient
from api.dummyjson.clients.products_client import ProductsClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("DUMMYJSON_API_URL", "https://dummyjson.com")


@pytest.fixture
def products_client(base_url):
    return ProductsClient(base_url=base_url)


@pytest.fixture
def auth_client(base_url):
    return AuthClient(base_url=base_url)


@pytest.fixture
def valid_token(auth_client):
    response = auth_client.login("emazit", "0lelplR")
    assert response.status_code == 200
    return response.json()["token"]
