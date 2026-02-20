from appium.webdriver.common.appiumby import AppiumBy


class OnboardingScreen:

    def __init__(self, driver):
        self.driver = driver

    def pass_if_present(self):
        skip_btns = self.driver.find_elements(
            AppiumBy.ID,
            "org.wikipedia.alpha:id/fragment_onboarding_skip_button"
        )
        if skip_btns:
            skip_btns[0].click()
        return self
