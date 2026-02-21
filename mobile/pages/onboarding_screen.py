from appium.webdriver.common.appiumby import AppiumBy

from mobile.pages.base_page import BasePage


class OnboardingScreen(BasePage):
    SKIP = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")

    def pass_if_present(self):
        if self.driver.find_elements(*self.SKIP):
            self.click(self.SKIP)
        return self
