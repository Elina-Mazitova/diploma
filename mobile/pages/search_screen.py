from appium.webdriver.common.appiumby import AppiumBy

from mobile.pages.base_page import BasePage


class SearchScreen(BasePage):
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    FIRST_RESULT = (AppiumBy.XPATH, "//android.widget.TextView[1]")
    ANY_RESULT = (AppiumBy.XPATH, "//android.widget.TextView")

    def type_query(self, text: str):
        return self.type(self.SEARCH_INPUT, text)

    def results_should_be_visible(self):
        return self.should_be_visible(self.ANY_RESULT)

    def open_first_result(self):
        return self.click(self.FIRST_RESULT)

    def get_first_result_text(self):
        return self.find(self.FIRST_RESULT).text
