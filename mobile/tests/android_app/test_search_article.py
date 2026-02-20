import allure

from mobile.helpers.onboarding_screen import OnboardingScreen
from mobile.helpers.main_screen import MainScreen
from mobile.helpers.search_screen import SearchScreen


@allure.title("Wikipedia: результаты поиска отображаются")
@allure.tag("mobile", "wikipedia", "search")
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
