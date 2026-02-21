import pytest
import os
from dotenv import load_dotenv
from selene import browser

from ui.data.credentials import TODOIST_LOGIN, TODOIST_PASSWORD
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.utils.browser import start_browser, stop_browser


load_dotenv()

browser.config.base_url = os.getenv("UI_BASE_URL")


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    start_browser()
    yield
    stop_browser()


@pytest.fixture
def authorized_user():
    login_page = LoginPage()
    main_page = MainPage()

    login_page.open().login(TODOIST_LOGIN, TODOIST_PASSWORD)

    return main_page
