import json
import pathlib

import allure
import pytest
from jsonschema import validate

from api.fakestore.models.request.product_request import ProductRequest
from api.fakestore.models.response.product_response import ProductResponse

pytestmark = pytest.mark.skip("FakeStore API returns 403 in CI environment")

SCHEMAS_DIR = pathlib.Path(__file__).parent.parent / "schemas"


def load_schema(name: str):
    with open(SCHEMAS_DIR / name, "r", encoding="utf-8") as file:
        return json.load(file)


@allure.feature("FakeStore API")
@allure.story("GET /products")
def test_get_products(products_client):
    with allure.step("Отправляем запрос на получение списка продуктов"):
        response = products_client.get_products()

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        validate(response.json(), load_schema("products_list.json"))


@allure.feature("FakeStore API")
@allure.story("GET /products/{id}")
@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(products_client, product_id):
    with allure.step(f"Отправляем запрос на получение продукта {product_id}"):
        response = products_client.get_product_by_id(product_id)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем модель ответа"):
        ProductResponse(**response.json())

    with allure.step("Валидируем схему ответа"):
        validate(response.json(), load_schema("product_response.json"))


@allure.feature("FakeStore API")
@allure.story("POST /products")
def test_create_product(products_client):
    payload = ProductRequest(
        title="New Product",
        price=9.99,
        description="Test product",
        category="test",
        image="https://example.com/image.jpg"
    )

    with allure.step("Валидируем request-схему"):
        validate(payload.model_dump(), load_schema("product_request.json"))

    with allure.step("Отправляем запрос на создание продукта"):
        response = products_client.create_product(payload.model_dump())

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 201

    with allure.step("Валидируем модель ответа"):
        ProductResponse(**response.json())

    with allure.step("Валидируем схему ответа"):
        validate(response.json(), load_schema("product_created.json"))


@allure.feature("FakeStore API")
@allure.story("PUT /products/{id}")
def test_update_product(products_client):
    payload = ProductRequest(
        title="Updated Product",
        price=11.99,
        description="Updated description",
        category="updated",
        image="https://example.com/image.jpg"
    )

    with allure.step("Валидируем request-схему"):
        validate(payload.model_dump(), load_schema("product_request.json"))

    with allure.step("Отправляем запрос на обновление продукта"):
        response = products_client.update_product(1, payload.model_dump())

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем модель ответа"):
        ProductResponse(**response.json())

    with allure.step("Валидируем схему ответа"):
        validate(response.json(), load_schema("product_updated.json"))


@allure.feature("FakeStore API")
@allure.story("DELETE /products/{id}")
def test_delete_product(products_client):
    with allure.step("Отправляем запрос на удаление продукта"):
        response = products_client.delete_product(1)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        validate(response.json(), load_schema("product_deleted.json"))
