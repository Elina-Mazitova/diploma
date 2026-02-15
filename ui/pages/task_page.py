from selene import browser, have, be
import allure



class TaskPage:

    add_task_button = browser.element('//button[.//span[text()="Добавить задачу"]]')
    task_input = browser.element('[data-placeholder]')
    submit_task_button = browser.element('[data-testid="task-editor-submit-button"]')
    tasks = browser.all('.task_content')

    @allure.step("Создать задачу: {text}")
    def create_task(self, text):
        browser.element('button.plus_add_button').should(be.visible).click()
        browser.element('[data-placeholder]').should(be.visible).type(text)
        browser.element('[data-testid="task-editor-submit-button"]').should(be.visible).click()

        return self

    @allure.step("Создать задачу с дедлайном: {text}")
    def create_task_with_due_date(self, text):
        self.add_task_button.click()
        self.task_input.type(text)

        browser.element('//div[text()="Срок"]').should(be.visible).click()
        browser.element(
            '//div[@class="scheduler-suggestions-item-label" and text()="Завтра"]'
        ).should(be.visible).click()

        self.submit_task_button.click()
        return self

    @allure.step("Проверить, что задача '{text}' появилась в списке")
    def should_see_task(self, text):
        self.tasks.element_by(have.text(text)).should(be.visible)
        return self

    @allure.step("Проверить, что у задачи '{text}' установлен дедлайн '{due}'")
    def should_have_due_date(self, text, due):
        self.tasks.element_by(have.text(text)).should(be.visible)
        browser.element(f'//span[text()="{due}"]').should(be.visible)
        return self

    @allure.step("Удалить задачу '{text}'")
    def delete_task(self, text):
        task = self.tasks.element_by(have.text(text))
        task.should(be.visible).click()

        menu_button = browser.element(
            '//div[@data-testid="button-container"]//button[@aria-label="Другие действия"]'
        )
        menu_button.should(be.visible).click()

        browser.element('//div[text()="Удалить"]').should(be.visible).click()
        browser.element('//button[.//span[text()="Удалить"]]').should(be.visible).click()

        return self

    @allure.step("Проверить, что задача '{text}' удалена")
    def should_not_see_task(self, text):
        self.tasks.should(have.no.text(text))
        return self

    @allure.step("Редактировать задачу '{old}' → '{new}'")
    def edit_task(self, old, new):
        # 1. Кликаем по задаче в списке
        task = self.tasks.element_by(have.text(old))
        task.should(be.visible).click()

        title = browser.element('//div[contains(@class, "task-overview-content-large")]')
        title.should(be.visible).click()

        editor = browser.element('//div[@data-typist-editor="true"]')
        editor.should(be.visible).clear().type(new)

        save_button = browser.element('//button[@data-testid="task-editor-submit-button"]')
        save_button.should(be.visible).click()

        return self

    @allure.step("Проверить, что задача обновилась на '{new}'")
    def should_see_updated_task(self, new):
        browser.element(
            f'//div[contains(@class, "task_content") and text()="{new}"]'
        ).should(be.visible)
        return self

