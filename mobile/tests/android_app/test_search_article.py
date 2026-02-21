import allure
import pytest

from mobile.config import load_config
from mobile.pages.main_screen import MainScreen
from mobile.pages.onboarding_screen import OnboardingScreen
from mobile.pages.search_screen import SearchScreen

config = load_config()


@pytest.mark.skipif(config["context"] == "local_real", reason="Поиск пропущен на реальном устройстве")
@allure.title("Wikipedia: результаты поиска отображаются")
def test_search_results_visible(mobile_management):
    driver = mobile_management

    OnboardingScreen(driver).pass_if_present()
    MainScreen(driver).should_be_opened().open_search()

    result_text = (
        SearchScreen(driver)
        .type_query("Python")
        .results_should_be_visible()
        .get_first_result_text()
    )

    assert result_text != "", "Первый результат поиска не найден"
