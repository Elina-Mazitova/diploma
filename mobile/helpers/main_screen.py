from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainScreen:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def should_be_opened(self):
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_container")
            )
        )
        return self

    def open_search(self):
        search_container = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_container")
            )
        )
        search_container.click()
        return self
