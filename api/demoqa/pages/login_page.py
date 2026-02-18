import time
import allure
from selene import browser, have, be


class LoginPage:

    @allure.step("Открываем страницу логина через главную страницу DemoQA")
    def open(self):
        with allure.step("Открываем главную страницу"):
            browser.open("https://demoqa.com/")

        with allure.step("Скроллим вниз, чтобы увидеть карточки"):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with allure.step("Закрываем поп‑ап, если он появился"):
            browser.execute_script("""
                const btn = document.evaluate("//button[text()='Close']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (btn) btn.click();
            """)

        with allure.step("Скрываем рекламный баннер и футер"):
            browser.execute_script("document.getElementById('fixedban').style.display='none';")
            browser.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

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

    @allure.step("Выполняем логин в UI")
    def login(self, username: str, password: str):
        browser.element("#userName").type(username)
        browser.element("#password").type(password)
        browser.element("#login").click()
        return self

    @allure.step("Проверяем, что пользователь '{username}' успешно авторизован")
    def should_be_logged_in_as(self, username: str):
        browser.element("#userName-value").should(have.text(username))
