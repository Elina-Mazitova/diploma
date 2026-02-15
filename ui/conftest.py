import pytest
from selene import browser
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.credentials import TODOIST_LOGIN, TODOIST_PASSWORD


@pytest.fixture(autouse=True)
def reset_browser():
    browser.open('about:blank')
    browser.driver.delete_all_cookies()
    yield
    browser.quit()

@pytest.fixture
def authorized_user():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.open_login_page().login(TODOIST_LOGIN, TODOIST_PASSWORD)

    return main_page

