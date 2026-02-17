from selene import browser, have, be
import allure


class ProjectPage:

    @allure.step("Перейти на страницу 'Мои проекты'")
    def open_projects_page(self):
        browser.element('//a[@href="/app/projects"]').should(be.visible).click()
        return self

    @allure.step("Открыть меню 'Добавить'")
    def open_add_menu(self):
        add_button = browser.element('//button[.//span[text()="Добавить"]]').should(be.visible)
        browser.driver.execute_script("arguments[0].click();", add_button())
        return self

    @allure.step("Выбрать 'Добавить проект'")
    def select_add_project(self):
        browser.element('//div[text()="Добавить проект"]').should(be.visible).click()
        return self

    @allure.step("Создать проект '{name}'")
    def create_project(self, name):
        self.open_projects_page()
        self.open_add_menu()
        self.select_add_project()

        modal = browser.element('//div[@role="dialog"]').should(be.visible)

        modal.element('.//input[@name="name"]').should(be.visible).type(name)

        modal.element('.//button[@type="submit" and .//span[text()="Добавить"]]').click()

        return self

    @allure.step("Проверить, что проект '{name}' появился в списке")
    def should_see_project(self, name):
        browser.element(f'//span[text()="{name}"]').should(be.visible)
        return self
