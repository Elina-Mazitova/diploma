import allure
import pytest

from ui.data.credentials import TODOIST_LOGIN, TODOIST_PASSWORD
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage


@allure.tag("UI")
@allure.feature("Авторизация")
@allure.story("Успешный вход")
def test_successful_login():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.open().login(TODOIST_LOGIN, TODOIST_PASSWORD)
    main_page.should_be_logged_in()


@allure.tag("UI")
@allure.feature("Авторизация")
@allure.story("Параметризованные негативные проверки")
@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        ("wrong@mail.com", "wrongpass", "Wrong email or password."),
        ("test@mail.com", "", "Passwords must be at least 8 characters long."),
    ],
)
def test_negative_login_parametrized(email, password, expected_error):
    login_page = LoginPage()

    login_page.open().login(email, password)
    login_page.should_see_error(expected_error)
