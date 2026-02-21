import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from mobile.utils.onboarding import get_text
from mobile.utils.onboarding import onboarding_present


@pytest.mark.no_skip_onboarding
def test_onboarding_full(mobile_management):
    driver = mobile_management
    package = driver.capabilities["appPackage"]

    if not onboarding_present(driver, package):
        pytest.skip("Onboarding is not shown on this device")

    forward_btn = f"{package}:id/fragment_onboarding_forward_button"

    text1 = get_text(driver, package)
    assert any(x in text1 for x in [
        "The Free Encyclopedia",
        "Свободная энциклопедия",
        "…более, чем на 300 языках"
    ])
    driver.find_element(AppiumBy.ID, forward_btn).click()
    time.sleep(1)
    text2 = get_text(driver, package)
    assert any(x in text2 for x in [
        "New ways to explore",
        "Мы нашли следующие языки",
        "Новые способы исследований",
        "Списки для чтения с синхронизацией"
    ])
    driver.find_element(AppiumBy.ID, forward_btn).click()

    time.sleep(1)
    text3 = get_text(driver, package)
    assert any(x in text3 for x in [
        "Reading lists with sync",
        "Списки для чтения с синхронизацией"
    ])
    driver.find_element(AppiumBy.ID, forward_btn).click()

    time.sleep(1)
    text4 = get_text(driver, package)
    assert any(x in text4 for x in [
        "Data & Privacy",
        "Добавить или удалить язык",
        "Данные и конфиденциальность"
    ])

    driver.find_element(AppiumBy.ID, f"{package}:id/fragment_onboarding_done_button").click()

    home = driver.find_elements(AppiumBy.ID, f"{package}:id/main_toolbar_wordmark")
    assert home, "Home screen did not appear after full onboarding"


@pytest.mark.no_skip_onboarding
def test_onboarding_skip(mobile_management):
    driver = mobile_management
    package = driver.capabilities["appPackage"]

    if not onboarding_present(driver, package):
        pytest.skip("Onboarding is not shown on this device")

    skip_btns = driver.find_elements(AppiumBy.ID, f"{package}:id/fragment_onboarding_skip_button")
    assert skip_btns, "Skip button is not shown on onboarding"

    skip_btns[0].click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.ID, f"{package}:id/main_toolbar_wordmark"))
    )
