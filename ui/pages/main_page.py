import allure
from selene import browser, be


class MainPage:
    path = "/app/"

    inbox_header = browser.element('//h1[text()="Входящие"]')

    @allure.step("Открыть главную страницу")
    def open(self):
        browser.open(self.path)
        return self

    @allure.step("Проверить, что пользователь успешно авторизован")
    def should_be_logged_in(self):
        browser.with_(timeout=10).wait_until(
            lambda _: "/app/" in browser.driver.current_url
        )
        self.inbox_header.should(be.visible)
        return self
