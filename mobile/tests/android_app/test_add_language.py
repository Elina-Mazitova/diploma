import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from mobile.pages.onboarding_screen import OnboardingScreen


@allure.title("Settings: add language (real device + BrowserStack)")
def test_add_language(mobile_management):
    driver = mobile_management
    wait = WebDriverWait(driver, 20)

    OnboardingScreen(driver).pass_if_present()

    is_bstack = "bstack:options" in driver.capabilities

    target_lang = "Русский" if is_bstack else "English"

    existing = driver.find_elements(
        AppiumBy.XPATH,
        f"//android.widget.TextView[contains(@text,'{target_lang}')]"
    )

    if existing:
        assert existing[0].is_displayed()
        return

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='More' or @text='Ещё']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Settings' or @text='Настройки']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Wikipedia languages' or @text='Языки Википедии']"
    ))).click()

    existing = driver.find_elements(
        AppiumBy.XPATH,
        f"//android.widget.TextView[contains(@text,'{target_lang}')]"
    )
    if existing:
        assert existing[0].is_displayed()
        return

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='Add language' or @text='Добавить язык']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        f"//android.widget.TextView[contains(@text,'{target_lang}')]"
    ))).click()

    added = wait.until(EC.presence_of_element_located((
        AppiumBy.XPATH,
        f"//android.widget.TextView[contains(@text,'{target_lang}')]"
    )))
    assert added.is_displayed()
