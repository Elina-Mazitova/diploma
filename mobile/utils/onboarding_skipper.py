from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mobile.utils.onboarding import onboarding_present


def skip_onboarding(driver, package):
    if not onboarding_present(driver, package):
        return

    wait = WebDriverWait(driver, 3)

    skip_btn = (AppiumBy.ID, f"{package}:id/fragment_onboarding_skip_button")
    forward_btn = (AppiumBy.ID, f"{package}:id/fragment_onboarding_forward_button")
    done_btn = (AppiumBy.ID, f"{package}:id/fragment_onboarding_done_button")

    skip_elements = driver.find_elements(*skip_btn)
    if skip_elements:
        skip_elements[0].click()
        return

    for _ in range(5):
        forward_elements = driver.find_elements(*forward_btn)
        if not forward_elements:
            break
        forward_elements[0].click()

    done_elements = driver.find_elements(*done_btn)
    if done_elements:
        done_elements[0].click()