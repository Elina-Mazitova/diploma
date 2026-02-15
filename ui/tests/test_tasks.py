import allure


@allure.tag("UI")
@allure.feature("Задачи")
@allure.story("Создание задачи")

def test_create_task(authorized_user):
    task_text = "тест задача"

    authorized_user.create_task(task_text) \
                   .should_see_task(task_text)

