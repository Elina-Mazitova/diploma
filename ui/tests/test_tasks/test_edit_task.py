import allure
from ui.pages.task_page import TaskPage

@allure.tag("UI")
@allure.feature("Задачи")
@allure.story("Редактирование задачи")
def test_edit_task(authorized_user):
    old_text = "задача три"
    new_text = "задача три исправленный"

    TaskPage() \
        .create_task(old_text) \
        .edit_task(old_text, new_text) \
        .should_see_updated_task(new_text)