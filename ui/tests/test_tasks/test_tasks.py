import allure
from selene import be, browser

from ui.pages.task_page import TaskPage


@allure.epic("UI")
@allure.feature("Задачи")
class TestTasks:

    @allure.story("Создание задачи")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ui", "tasks")
    def test_create_task(self, authorized_user):
        page = TaskPage()
        page.add_task_button.wait_until(be.present)
        page.add_task_button.wait_until(be.visible)
        browser.element('.rtbnZ8S').wait_until(be.not_.visible)
        page.create_task("тест задача")
        page.should_see_task("тест задача")

    @allure.story("Создание задачи с дедлайном через календарь")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ui", "tasks", "due_date")
    def test_create_task_with_due_date(self, authorized_user):
        page = TaskPage()
        page.add_task_button.wait_until(be.present)
        page.add_task_button.wait_until(be.visible)
        browser.element('.rtbnZ8S').wait_until(be.not_.visible)
        page.create_task_with_due_date("задача два")
        page.should_see_task("задача два")
        page.should_have_due_date("задача два", "Завтра")

    @allure.story("Удаление задачи")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ui", "tasks", "delete")
    def test_delete_task(self, authorized_user):
        page = TaskPage()
        page.add_task_button.wait_until(be.present)
        page.add_task_button.wait_until(be.visible)
        browser.element('.rtbnZ8S').wait_until(be.not_.visible)
        page.create_task("тест задача четыре")
        page.delete_task("тест задача четыре")
        page.should_not_see_task("тест задача четыре")

    @allure.story("Редактирование задачи")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ui", "tasks", "edit")
    def test_edit_task(self, authorized_user):
        page = TaskPage()
        page.add_task_button.wait_until(be.present)
        page.add_task_button.wait_until(be.visible)
        page.create_task("задача три")
        browser.element('.rtbnZ8S').wait_until(be.not_.visible)
        page.edit_task("задача три", "задача три изменена")
        page.should_see_task("задача три изменена")
