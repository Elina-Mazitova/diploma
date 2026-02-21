import os

import pytest
from dotenv import load_dotenv

from api.dummyjson.clients.products_client import ProductsClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("DUMMYJSON_API_URL", "https://dummyjson.com")


@pytest.fixture
def products_client(base_url):
    return ProductsClient(base_url=base_url)
