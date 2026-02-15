from selene import browser, have, be
from .base_page import BasePage
import allure


class MainPage(BasePage):

    inbox_header = browser.element('h1.bff24867')

    @allure.step("Проверить, что пользователь успешно авторизован")
    def should_be_logged_in(self):
        # Ждём перехода на приложение
        browser.with_(timeout=10).wait_until(
            lambda _: '/app/' in browser.driver.current_url
        )

        # Ждём появления заголовка
        self.inbox_header.should(be.visible)

        # Ждём появления текста (главное!)
        self.inbox_header.should(have.text('Входящие'))

        return self
