import allure
from selene import browser, be


class LoginPage:
    path = "/auth/login"

    email_input = browser.element('input[type="email"]')
    password_input = browser.element('input[type="password"]')
    submit_button = browser.element('button[type="submit"]')

    def error_message(self, text):
        return browser.element(f'//*[text()="{text}"]')

    @allure.step("Открыть страницу логина")
    def open(self):
        browser.open(self.path)
        return self

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.email_input.should(be.visible).type(email)
        self.password_input.should(be.visible).type(password)
        self.submit_button.should(be.clickable).click()
        return self

    @allure.step("Проверить отображение ошибки: {message}")
    def should_see_error(self, message):
        self.error_message(message).should(be.visible)
        return self
