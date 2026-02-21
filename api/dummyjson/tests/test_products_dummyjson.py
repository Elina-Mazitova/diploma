import json
import pathlib

import allure
import jsonschema
import pytest

from api.dummyjson.models.request.product_request import ProductRequest


def load_schema(name: str):
    path = pathlib.Path(__file__).parent.parent / "schemas" / name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@allure.feature("DummyJSON API")
@allure.story("GET /products")
def test_get_products(products_client):
    with allure.step("Отправляем запрос на получение списка продуктов"):
        response = products_client.get_products()

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            response.json(),
            load_schema("products_list.json")
        )


@allure.feature("DummyJSON API")
@allure.story("GET /products/{id}")
@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(products_client, product_id):
    with allure.step(f"Отправляем запрос на получение продукта {product_id}"):
        response = products_client.get_product_by_id(product_id)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            response.json(),
            load_schema("product_response.json")
        )

    with allure.step("Проверяем корректность id"):
        assert response.json()["id"] == product_id


@allure.feature("DummyJSON API")
@allure.story("POST /products/add")
def test_create_product(products_client):
    payload = ProductRequest(
        title="New Product",
        price=9.99,
        description="Test product",
        category="test",
        thumbnail="https://example.com/image.jpg"
    )

    with allure.step("Валидируем request-схему"):
        jsonschema.validate(
            payload.model_dump(),
            load_schema("product_request.json")
        )

    with allure.step("Отправляем запрос на создание продукта"):
        response = products_client.create_product(payload.model_dump())

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 201

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            response.json(),
            load_schema("product_created.json")
        )

    with allure.step("Проверяем корректность title"):
        assert response.json()["title"] == "New Product"


@allure.feature("DummyJSON API")
@allure.story("PUT /products/{id}")
def test_update_product(products_client):
    payload = ProductRequest(
        title="Updated Product",
        price=19.99,
        description="Updated description",
        category="updated",
        thumbnail="https://example.com/image.jpg"
    )

    with allure.step("Валидируем request-схему"):
        jsonschema.validate(
            payload.model_dump(),
            load_schema("product_request.json")
        )

    with allure.step("Отправляем запрос на обновление продукта"):
        response = products_client.update_product(1, payload.model_dump())

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            response.json(),
            load_schema("product_response.json")
        )

    with allure.step("Проверяем корректность title"):
        assert response.json()["title"] == "Updated Product"


@allure.feature("DummyJSON API")
@allure.story("DELETE /products/{id}")
def test_delete_product(products_client):
    with allure.step("Отправляем запрос на удаление продукта"):
        response = products_client.delete_product(1)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            response.json(),
            load_schema("product_response.json")
        )

    with allure.step("Проверяем корректность id"):
        assert response.json()["id"] == 1
