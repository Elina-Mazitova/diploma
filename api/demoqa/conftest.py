import os

import pytest
from dotenv import load_dotenv
from selene import browser

from api.demoqa.clients.auth_client import AuthClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("DEMOQA_API_URL", "https://demoqa.com")


@pytest.fixture
def auth_client(base_url):
    return AuthClient(base_url=base_url)


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.timeout = 10
    browser.config.window_width = 1400
    browser.config.window_height = 900