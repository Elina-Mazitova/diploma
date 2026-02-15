from selene import browser, have, be
from .base_page import BasePage
import allure


class MainPage(BasePage):

    inbox_header = browser.element('h1.bff24867')

    @allure.step("Проверить, что пользователь успешно авторизован")
    def should_be_logged_in(self):
        browser.with_(timeout=10).wait_until(
            lambda _: '/app/' in browser.driver.current_url
        )

        self.inbox_header.should(be.visible)

        self.inbox_header.should(have.text('Входящие'))

        return self
