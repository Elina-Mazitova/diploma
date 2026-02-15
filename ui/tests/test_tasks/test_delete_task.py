import allure
from ui.pages.task_page import TaskPage

@allure.tag("UI")
@allure.feature("Задачи")
@allure.story("Удаление задачи")
def test_delete_task(authorized_user):
    task_text = "тест задача четыре"

    TaskPage() \
        .create_task(task_text) \
        .delete_task(task_text) \
        .should_not_see_task(task_text)