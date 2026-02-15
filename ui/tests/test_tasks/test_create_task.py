import allure
from ui.pages.task_page import TaskPage


@allure.tag("UI")
@allure.feature("Задачи")
@allure.story("Создание задачи")

def test_create_task(authorized_user):
    task_text = "тест задача"

    TaskPage() \
        .create_task(task_text) \
        .should_see_task(task_text)
