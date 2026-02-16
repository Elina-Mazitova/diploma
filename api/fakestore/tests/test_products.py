import json
import pytest
from jsonschema import validate

from api.fakestore.models.request.product_request import ProductRequest
from api.fakestore.models.response.product_response import ProductResponse


def test_get_products(products_client):
    response = products_client.get_products()
    assert response.status_code == 200

    body = response.json()

    with open("api/fakestore/schemas/products_list.json") as file:
        schema = json.load(file)

    validate(instance=body, schema=schema)


@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(products_client, product_id):
    response = products_client.get_product_by_id(product_id)
    assert response.status_code == 200

    ProductResponse(**response.json())

    with open("api/fakestore/schemas/product_by_id.json") as file:
        schema = json.load(file)

    validate(instance=response.json(), schema=schema)



def test_create_product(products_client):
    payload = ProductRequest(
        title="New Product",
        price=9.99,
        description="Test product",
        category="test",
        image="http://example.com"
    )

    response = products_client.create_product(payload.model_dump())
    assert response.status_code == 201

    ProductResponse(**response.json())

    with open("api/fakestore/schemas/product_created_or_updated.json") as file:
        schema = json.load(file)

    validate(instance=response.json(), schema=schema)


def test_update_product(products_client):
    payload = ProductRequest(
        title="Updated Product",
        price=11.99,
        description="Dog",
        category="Yellow",
        image="http://examples.com"
    )

    response = products_client.update_product(1, payload.model_dump())
    assert response.status_code == 200

    ProductResponse(**response.json())

    with open("api/fakestore/schemas/product_created_or_updated.json") as file:
        schema = json.load(file)

    validate(instance=response.json(), schema=schema)


def test_update_product_incorrect(products_client):
    payload = ProductRequest(
        title="Updated Product",
        price=11.99,
        description="Dog",
        category="Yellow",
        image="http://examples.com"
    )

    response = products_client.update_product("1-", payload.model_dump())
    assert response.status_code == 400

    with open("api/fakestore/schemas/product_updated_invalid.json") as file:
        schema = json.load(file)

    validate(instance=response.json(), schema=schema)


def test_delete_product(products_client):
    response = products_client.delete_product(1)
    assert response.status_code == 200


def test_delete_product_incorrect_id(products_client):
    response = products_client.delete_product("1-")
    assert response.status_code == 400
