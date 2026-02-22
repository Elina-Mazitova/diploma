import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scroll_to_text(driver, text):
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{text}")'
    )


@allure.title("Settings: add language (real device + BrowserStack)")
def test_add_language(mobile_management):
    driver = mobile_management
    wait = WebDriverWait(driver, 20)

    is_bstack = "bstack:options" in driver.capabilities
    target_lang_ru = "Русский"
    target_lang_en = "Russian"

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, "//android.widget.TextView[@text='More' or @text='Ещё']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, "//android.widget.TextView[@text='Settings' or @text='Настройки']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, "//android.widget.TextView[@text='Wikipedia languages' or @text='Языки Википедии']"
    ))).click()

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, "//android.widget.TextView[@text='Add language' or @text='Добавить язык']"
    ))).click()

    scroll_to_text(driver, target_lang_en)

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, f"//*[contains(@text,'{target_lang_en}')]"
    ))).click()

    added = wait.until(EC.presence_of_element_located((
        AppiumBy.XPATH, f"//*[contains(@text,'{target_lang_ru}')]"
    )))
    assert added.is_displayed()
