import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Settings: add Russian language")
def test_add_russian_language(mobile_management):
    driver = mobile_management
    wait = WebDriverWait(driver, 20)

    with allure.step("Skip onboarding"):
        skip_btns = driver.find_elements(AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        if skip_btns:
            skip_btns[0].click()

    with allure.step("Open More menu"):
        more_btn = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='More']")
            )
        )
        more_btn.click()

    with allure.step("Open Settings"):
        settings_btn = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']")
            )
        )
        settings_btn.click()

    with allure.step("Open Wikipedia languages"):
        wiki_lang_btn = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Wikipedia languages']")
            )
        )
        wiki_lang_btn.click()

    with allure.step("Tap Add language"):
        add_lang_btn = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Add language']")
            )
        )
        add_lang_btn.click()

    with allure.step("Select Russian"):
        russian_btn = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Русский']")
            )
        )
        russian_btn.click()

    with allure.step("Verify Russian is added"):
        russian_in_list = wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/wiki_language_title' and @text='Русский']"
                )
            )
        )
        assert russian_in_list.is_displayed(), "Русский язык не появился в списке"
