import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.helpers.onboarding import onboarding_present



def skip_onboarding(driver, package):

    if not onboarding_present(driver, package):
        return

    try:
        skip_btn = driver.find_element(AppiumBy.ID, f"{package}:id/fragment_onboarding_skip_button")
        skip_btn.click()
        time.sleep(1)
        return
    except:
        pass

    forward_btn = f"{package}:id/fragment_onboarding_forward_button"
    done_btn = f"{package}:id/fragment_onboarding_done_button"

    for _ in range(5):
        try:
            driver.find_element(AppiumBy.ID, forward_btn).click()
            time.sleep(1)
        except:
            break

    try:
        driver.find_element(AppiumBy.ID, done_btn).click()
        time.sleep(1)
    except:
        pass
