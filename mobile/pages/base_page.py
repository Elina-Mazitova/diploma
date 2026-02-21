from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return self

    def type(self, locator, text: str):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.clear()
        element.send_keys(text)
        return self

    def should_be_visible(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return self

    def should_have_text(self, locator, expected_text: str):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        assert expected_text in element.text
        return self

    def scroll_to_text(self, text: str):
        scrollable = (
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            f'.scrollIntoView(new UiSelector().textContains("{text}").instance(0));'
        )
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable)
        return self
