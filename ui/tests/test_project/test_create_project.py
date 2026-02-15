import allure
from pages.project_page import ProjectPage


@allure.tag("UI")
@allure.feature("Проекты")
@allure.story("Создание проекта")
def test_create_project(authorized_user):
    ProjectPage() \
        .create_project("тест проект") \
        .should_see_project("тест проект")

