from selene import browser, have, be
from .base_page import BasePage
import allure


class LoginPage(BasePage):

    email_input = browser.element('#element-0')
    password_input = browser.element('#element-2')
    login_button = browser.element('button[type="submit"]')

    @allure.step("Открыть страницу логина Todoist")
    def open_login_page(self):
        self.open("https://app.todoist.com/auth/login")
        return self

    @allure.step("Авторизоваться в Todoist")
    def login(self, email, password):
        self.email_input.type(email)
        self.password_input.type(password)
        self.login_button.should(be.clickable).click()

        # Снимаем фокус, чтобы Todoist показал ошибку
        browser.element('body').click()

        return self

    @allure.step("Проверить сообщение об ошибке")
    def should_see_error(self, message):
        browser.all('.a83bd4e0').element_by(have.text(message)).should(be.visible)
        return self
