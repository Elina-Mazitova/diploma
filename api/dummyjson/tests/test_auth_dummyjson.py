import allure
import jsonschema

from api.dummyjson.models.request.login_request import LoginRequest
from api.dummyjson.models.response.login_response import LoginResponse
from api.dummyjson.tests.test_products_dummyjson import load_schema


@allure.feature("DummyJSON API")
@allure.story("POST /auth/login — успешная авторизация")
def test_login_success(auth_client):
    payload = LoginRequest(
        username="emilys",
        password="emilyspass"
    ).model_dump(by_alias=True)

    with allure.step("Отправляем запрос на авторизацию"):
        response = auth_client.login(**payload)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("Валидируем схему ответа"):
        jsonschema.validate(
            data,
            load_schema("login_response.json")
        )

    with allure.step("Проверяем наличие accessToken и refreshToken"):
        parsed = LoginResponse(**data)
        assert parsed.accessToken != ""
        assert parsed.refreshToken != ""


@allure.feature("DummyJSON API")
@allure.story("POST /auth/login — неверные данные")
def test_login_wrong_username(auth_client):
    payload = {
        "password": "whatever"
    }

    with allure.step("Отправляем запрос с некорректным телом"):
        response = auth_client.login_negative(**payload)

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 400

    with allure.step("Проверяем сообщение об ошибке"):
        assert response.json()["message"] == "Username and password required"
