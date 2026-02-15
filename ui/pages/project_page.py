from selene import browser, have, be
import allure


class ProjectPage:

    @allure.step("Открыть меню создания проекта (кнопка плюс)")
    def open_create_project_menu(self):
        browser.element('//div[text()="Мои проекты"]').hover()

        browser.element(
            '//div[text()="Мои проекты"]/following::button[@aria-label="Мои проекты"][1]'
        ).should(be.visible).click()

        return self

    @allure.step("Выбрать 'Добавить проект'")
    def click_add_project(self):
        browser.element('//div[text()="Добавить проект"]').should(be.visible).click()
        return self

    @allure.step("Создать проект '{name}'")
    def create_project(self, name):
        self.open_create_project_menu()
        self.click_add_project()

        browser.element('//input[@name="name"]').should(be.visible).type(name)
        browser.element('//button[.//span[text()="Добавить"]]').should(be.visible).click()

        return self

    @allure.step("Проверить, что проект '{name}' появился в списке")
    def should_see_project(self, name):
        browser.element(f'//span[text()="{name}"]').should(be.visible)
        return self
