import pytest
from utils.browser import start_browser, stop_browser
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.credentials import TODOIST_LOGIN, TODOIST_PASSWORD


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    start_browser()
    yield
    stop_browser()


@pytest.fixture
def authorized_user():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.open_login_page().login(TODOIST_LOGIN, TODOIST_PASSWORD)

    return main_page
