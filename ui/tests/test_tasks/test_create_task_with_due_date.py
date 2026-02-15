import allure
from pages.task_page import TaskPage


@allure.tag("UI")
@allure.feature("Задачи")
@allure.story("Создание задачи с дедлайном через календарь")
def test_create_task_with_due_date(authorized_user):
    task_text = "задача два"

    TaskPage() \
        .create_task_with_due_date(task_text) \
        .should_see_task(task_text) \
        .should_have_due_date(task_text, "Завтра")