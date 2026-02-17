import os
import allure
from allure_commons.types import AttachmentType

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))


def start_browser():
    user = os.getenv("SELENOID_USER")
    password = os.getenv("SELENOID_PASSWORD")
    host = os.getenv("SELENOID_HOST")

    use_selenoid = all([user, password, host])

    if use_selenoid:
        remote_url = f"https://{user}:{password}@{host}"

        options = Options()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")

        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        })

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )

    else:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.timeout = float(os.getenv("TIMEOUT", "10"))
    browser.config.base_url = "https://demoqa.com"


def stop_browser():
    driver = browser.driver

    attach_screenshot(driver)
    attach_page_source(driver)
    attach_logs(driver)
    attach_video(driver)

    browser.quit()


def attach_screenshot(driver):
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )
    except Exception as e:
        allure.attach(str(e), "screenshot_error", AttachmentType.TEXT)


def attach_page_source(driver):
    try:
        allure.attach(
            driver.page_source,
            name="page_source",
            attachment_type=AttachmentType.HTML
        )
    except Exception as e:
        allure.attach(str(e), "page_source_error", AttachmentType.TEXT)


def attach_logs(driver):
    try:
        logs = driver.execute("getLog", {"type": "browser"})["value"]
        formatted = "".join(f"{line}\n" for line in logs)

        allure.attach(
            formatted,
            name="browser_logs",
            attachment_type=AttachmentType.TEXT,
            extension=".log"
        )
    except Exception as e:
        allure.attach(str(e), "browser_logs_error", AttachmentType.TEXT)


def attach_video(driver):
    try:
        session_id = driver.session_id
        video_host = os.getenv("SELENOID_VIDEO_HOST", "selenoid.autotests.cloud")

        video_url = f"https://{video_host}/video/{session_id}.mp4"

        html = (
            "<html><body>"
            "<video width='100%' height='100%' controls autoplay>"
            f"<source src='{video_url}' type='video/mp4'>"
            "</video>"
            "</body></html>"
        )

        allure.attach(
            html,
            name=f"video_{session_id}",
            attachment_type=AttachmentType.HTML
        )
    except Exception as e:
        allure.attach(str(e), "video_error", AttachmentType.TEXT)
