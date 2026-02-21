import json
import pathlib
import uuid

import allure
import jsonschema
import pytest

from api.demoqa.models.request.login_request import LoginRequest
from api.demoqa.models.request.user_create_request import UserCreateRequest
from api.demoqa.models.response.token_response import TokenResponse
from api.demoqa.pages.login_page import LoginPage
from api.demoqa.utils.browser import start_browser, stop_browser


def load_schema(name: str) -> dict:
    path = pathlib.Path(__file__).parent.parent / "schemas" / name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    start_browser()
    yield
    stop_browser()


@allure.feature("Авторизация")
@allure.story("API → UI интеграция")
def test_api_to_ui_login(auth_client):
    with allure.step("Генерируем тестовые данные"):
        username = f"ElinaUser_{uuid.uuid4().hex[:6]}"
        password = "StrongPass123!"

    with allure.step("Создаём пользователя через API"):
        create_body = UserCreateRequest(
            userName=username,
            password=password
        )

        jsonschema.validate(
            create_body.model_dump(),
            load_schema("user_create_request.json")
        )

        create_response = auth_client.create_user(create_body.model_dump())
        assert create_response.status_code == 201

        jsonschema.validate(
            create_response.json(),
            load_schema("user_create_response.json")
        )

        assert create_response.json()["userID"], "userID должен быть непустым"

    with allure.step("Генерируем токен через API"):
        login_body = LoginRequest(
            userName=username,
            password=password
        )

        jsonschema.validate(
            login_body.model_dump(),
            load_schema("login_request.json")
        )

        token_response = auth_client.generate_token(login_body.model_dump())
        assert token_response.status_code == 200

        jsonschema.validate(
            token_response.json(),
            load_schema("login_response.json")
        )

        token_data = TokenResponse(**token_response.json())
        assert token_data.status == "Success"
        assert token_data.token, "token должен быть непустым"

    with allure.step("Проверяем логин через API"):
        login_response = auth_client.login(login_body.model_dump())
        assert login_response.status_code == 200

        jsonschema.validate(
            login_response.json(),
            load_schema("login_success_response.json")
        )

        assert login_response.json()["username"] == username

    with allure.step("Авторизуемся в UI"):
        login_page = LoginPage()
        login_page.open().login(username, password)

    with allure.step("Проверяем успешный вход в UI"):
        login_page.should_be_logged_in_as(username)
