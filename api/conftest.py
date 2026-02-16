import pytest
from api.fakestore.clients.products_client import ProductsClient
from api.fakestore_auth.clients.auth_client import AuthClient

@pytest.fixture
def base_url():
    return "https://fakestoreapi.com"


@pytest.fixture
def products_client(base_url):
    return ProductsClient(base_url=base_url)

@pytest.fixture
def auth_client():
    return AuthClient()

