import allure
import pytest
import uuid

from api.demoqa.models.request.user_create_request import UserCreateRequest
from api.demoqa.models.request.login_request import LoginRequest
from api.demoqa.models.response.token_response import TokenResponse
from api.demoqa.pages.login_page import LoginPage

from api.demoqa.utils.browser import start_browser, stop_browser


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
        create_response = auth_client.create_user(create_body.model_dump())
        assert create_response.status_code == 201

    with allure.step("Генерируем токен через API"):
        login_body = LoginRequest(
            userName=username,
            password=password
        )
        token_response = auth_client.generate_token(login_body.model_dump())
        assert token_response.status_code == 200

        token_data = TokenResponse(**token_response.json())
        assert token_data.status == "Success"

    with allure.step("Проверяем логин через API"):
        login_response = auth_client.login(login_body.model_dump())
        assert login_response.status_code == 200

    with allure.step("Авторизуемся в UI"):
        login_page = LoginPage()
        login_page.open().login(username, password)

    with allure.step("Проверяем успешный вход в UI"):
        login_page.should_be_logged_in_as(username)
