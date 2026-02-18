import pytest
from api.dummyjson.clients.products_client import ProductsClient
from api.dummyjson.models.request.product_request import ProductRequest


@pytest.fixture
def products_client():
    return ProductsClient()


def test_get_products(products_client):
    response = products_client.get_products()
    assert response.status_code == 200
    assert "products" in response.json()


@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(products_client, product_id):
    response = products_client.get_product_by_id(product_id)
    assert response.status_code == 200
    assert response.json()["id"] == product_id


def test_create_product(products_client):
    payload = ProductRequest(
        title="New Product",
        price=9.99,
        description="Test product",
        category="test",
        thumbnail="https://example.com/image.jpg"
    )

    response = products_client.create_product(payload.model_dump())
    assert response.status_code == 201
    assert response.json()["title"] == "New Product"


def test_update_product(products_client):
    payload = ProductRequest(
        title="Updated Product",
        price=19.99,
        description="Updated description",
        category="updated",
        thumbnail="https://example.com/image.jpg"
    )

    response = products_client.update_product(1, payload.model_dump())
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Product"


def test_delete_product(products_client):
    response = products_client.delete_product(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
