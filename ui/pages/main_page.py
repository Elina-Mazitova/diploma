from selene import browser, have, be
from .base_page import BasePage
import allure


class MainPage(BasePage):

    inbox_header = browser.element('h1.bff24867')

    add_task_button = browser.element('//button[.//span[text()="Добавить задачу"]]')
    task_input = browser.element('[data-placeholder]')
    submit_task_button = browser.element('[data-testid="task-editor-submit-button"]')
    tasks = browser.all('.task_content')

    @allure.step("Проверить, что пользователь успешно авторизован")
    def should_be_logged_in(self):
        browser.with_(timeout=10).wait_until(
            lambda _: '/app/' in browser.driver.current_url
        )
        self.inbox_header.should(be.visible)
        self.inbox_header.should(have.text('Входящие'))
        return self

    @allure.step("Создать задачу: {text}")
    def create_task(self, text):
        self.add_task_button.click()
        self.task_input.type(text)
        self.submit_task_button.click()
        return self

    @allure.step("Проверить, что задача '{text}' появилась в списке")
    def should_see_task(self, text):
        self.tasks.element_by(have.text(text)).should(be.visible)
        return self
