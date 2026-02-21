import allure
from selene import browser, be, have
from selenium.webdriver.common.keys import Keys


class TaskPage:
    path = "/app/"

    add_task_button = browser.element('button.plus_add_button')
    task_input = browser.element('[data-placeholder]')
    submit_task_button = browser.element('[data-testid="task-editor-submit-button"]')
    task_items = browser.all('.task_content')

    @allure.step("Открыть страницу задач")
    def open(self):
        browser.open(self.path)
        return self

    @allure.step("Создать задачу: {text}")
    def create_task(self, text):
        self.open()
        self.add_task_button.should(be.visible).click()
        self.task_input.should(be.visible).type(text)
        self.submit_task_button.should(be.visible).click()
        return self

    @allure.step("Создать задачу с дедлайном: {text}")
    def create_task_with_due_date(self, text):
        self.open()
        self.add_task_button.should(be.visible).click()
        self.task_input.should(be.visible).type(text)
        browser.element('//div[text()="Срок"]').should(be.visible).click()
        browser.element('//div[@class="scheduler-suggestions-item-label" and text()="Завтра"]').should(
            be.visible).click()
        self.submit_task_button.should(be.visible).click()
        return self

    @allure.step("Проверить, что задача '{text}' появилась")
    def should_see_task(self, text):
        self.task_items.element_by(have.text(text)).should(be.visible)
        return self

    @allure.step("Проверить, что у задачи '{text}' установлен дедлайн '{due}'")
    def should_have_due_date(self, text, due):
        self.task_items.element_by(have.text(text)).should(be.visible)
        browser.element(f'//span[text()="{due}"]').should(be.visible)
        return self

    @allure.step("Удалить задачу '{text}'")
    def delete_task(self, text):
        task = self.task_items.element_by(have.text(text))
        task.should(be.visible).click()
        browser.element('//div[@data-testid="button-container"]//button[@aria-label="Другие действия"]').should(
            be.visible).click()
        browser.element('//div[text()="Удалить"]').should(be.visible).click()
        browser.element('//button[.//span[text()="Удалить"]]').should(be.visible).click()
        return self

    @allure.step("Проверить, что задача '{text}' удалена")
    def should_not_see_task(self, text):
        self.task_items.should(have.no.text(text))
        return self

    @allure.step("Редактировать задачу '{old}' → '{new}'")
    def edit_task(self, old, new):
        task = self.task_items.element_by(have.text(old))
        task.should(be.visible).click()
        title = browser.element('//div[@class="task_content task-overview-content-large"]')
        title.should(be.visible).click()
        editor = browser.driver.switch_to.active_element
        editor.send_keys(Keys.CONTROL, "a")
        editor.send_keys(Keys.DELETE)
        editor.send_keys(new)
        editor.send_keys(Keys.ENTER)
        return self

    @allure.step("Проверить, что задача обновилась на '{new}'")
    def should_see_updated_task(self, new):
        browser.element(f'//div[contains(@class, "task_content") and text()="{new}"]').should(be.visible)
        return self
