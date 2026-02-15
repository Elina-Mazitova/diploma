import allure
from ui.pages.login_page  import LoginPage
from ui.pages.main_page import MainPage
from data.credentials import TODOIST_LOGIN, TODOIST_PASSWORD


@allure.tag("UI")
@allure.feature("Авторизация")
@allure.story("Успешный вход")
def test_successful_login():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.open_login_page() \
              .login(TODOIST_LOGIN, TODOIST_PASSWORD)

    main_page.should_be_logged_in()


@allure.tag("UI")
@allure.feature("Авторизация")
@allure.story("Неверный пароль")
def test_login_with_wrong_password():
    login_page = LoginPage()

    login_page.open_login_page() \
              .login(TODOIST_LOGIN, "wrong_password") \
              .should_see_error("Неверный Email или пароль.")


@allure.tag("UI")
@allure.feature("Авторизация")
@allure.story("Пустой пароль")
def test_login_with_empty_fields():
    login_page = LoginPage()

    login_page.open_login_page() \
              .login(TODOIST_LOGIN, "") \
              .should_see_error("В пароле должно быть не менее 8 символов.")


