from appium.webdriver.common.appiumby import AppiumBy

from mobile.pages.base_page import BasePage


class MainScreen(BasePage):
    SEARCH_CONTAINER = (AppiumBy.ID, "org.wikipedia.alpha:id/search_container")

    def should_be_opened(self):
        return self.should_be_visible(self.SEARCH_CONTAINER)

    def open_search(self):
        return self.click(self.SEARCH_CONTAINER)
