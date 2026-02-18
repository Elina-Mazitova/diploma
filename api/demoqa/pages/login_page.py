import allure
from selene import browser, have, be


class LoginPage:

    @allure.step("Открываем страницу логина через главную страницу DemoQA")
    def open(self):
        with allure.step("Открываем главную страницу"):
            browser.open("https://demoqa.com/")

        with allure.step("Скроллим вниз, чтобы увидеть карточки"):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with allure.step("Ждём, вдруг поп‑ап сам исчезнет"):
            browser.sleep(3)

        with allure.step("Скрываем рекламный баннер и футер"):
            browser.execute_script("document.getElementById('fixedban').style.display='none';")
            browser.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

        with allure.step("Закрываем всплывающую рекламу, если она есть"):
            browser.execute_script("""
                const selectors = [
                    '#close-fixedban',
                    '.fc-dialog-container',
                    '.modal',
                    'div[role="dialog"]',
                    '.popup',
                    '.advertisement',
                    '.home-banner',
                    '.elementor-widget-container'
                ];
                selectors.forEach(sel => {
                    const el = document.querySelector(sel);
                    if (el) el.style.display = 'none';
                });
            """)

        with allure.step("Переходим в Book Store Application"):
            card = browser.element("//h5[text()='Book Store Application']")
            card.should(be.visible)
            card.click()

        with allure.step("Переходим на страницу логина"):
            login_button = browser.element("#login")
            login_button.should(be.visible)
            login_button.click()

        with allure.step("Проверяем, что форма логина отображается"):
            browser.element("#userName").should(be.visible)

        return self
