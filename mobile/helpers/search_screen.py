from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchScreen:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def type_query(self, text):
        search_input = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
            )
        )
        search_input.send_keys(text)
        return self

    def results_should_be_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView")
            )
        )
        return self

    def get_first_result_text(self):
        first_result = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[1]")
            )
        )
        return first_result.text
