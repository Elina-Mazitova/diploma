import pytest
from api.fakestore.clients.products_client import ProductsClient
from api.demoqa.clients.auth_client import AuthClient
from selene import browser

@pytest.fixture
def base_url():
    return "https://fakestoreapi.com"


@pytest.fixture
def products_client(base_url):
    return ProductsClient(base_url=base_url)


@pytest.fixture
def auth_client():
    return AuthClient(base_url="https://demoqa.com")

@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.timeout = 10
    browser.config.window_width = 1400
    browser.config.window_height = 900

