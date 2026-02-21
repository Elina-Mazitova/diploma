import allure

from ui.pages.project_page import ProjectPage


@allure.epic("UI")
@allure.feature("Проекты")
class TestProjects:

    @allure.story("Создание проекта")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ui", "projects")
    def test_create_project(self, authorized_user):
        page = ProjectPage()

        page.create_project("тест проект")

        page.should_see_project("тест проект")
