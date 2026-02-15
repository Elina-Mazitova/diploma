from selene import browser, have, be
import allure


class LoginPage:

    email_input = browser.element('//input[@type="email"]')
    password_input = browser.element('//input[@type="password"]')
    login_button = browser.element('//button[@type="submit"]')

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        browser.open("https://app.todoist.com/auth/login")
        return self

    @allure.step("Авторизоваться под пользователем {email}")
    def login(self, email, password):
        self.email_input.should(be.visible).type(email)
        self.password_input.should(be.visible).type(password)
        self.login_button.should(be.clickable).click()
        return self

    @allure.step("Проверить сообщение об ошибке")
    def should_see_error(self, message):
        browser.all('.a83bd4e0').element_by(have.text(message)).should(be.visible)
        return self
