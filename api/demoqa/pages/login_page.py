import allure
from selene import browser, be, have


class LoginPage:

    @allure.step("Открываем страницу логина через главную страницу DemoQA")
    def open(self):
        with allure.step("Открываем главную страницу"):
            browser.open("https://demoqa.com/")

        with allure.step("Удаляем рекламу (iframe + fixedban)"):
            browser.driver.execute_script("""
                document.querySelectorAll('iframe').forEach(el => el.remove());
                const ad = document.getElementById('fixedban');
                if (ad) ad.remove();
            """)

        with allure.step("Скроллим до карточки Book Store"):
            card = browser.element("//h5[text()='Book Store Application']/ancestor::a")
            browser.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card())

        with allure.step("Переходим в Book Store Application"):
            card.click()

        with allure.step("Удаляем рекламу на странице Book Store"):
            browser.driver.execute_script("""
                document.querySelectorAll('iframe').forEach(el => el.remove());
                const ad = document.getElementById('fixedban');
                if (ad) ad.remove();
            """)

        with allure.step("Переходим на страницу логина"):
            login_button = browser.element("#login")
            login_button.should(be.visible)
            login_button.click()

        with allure.step("Проверяем, что форма логина отображается"):
            browser.element("#userName").should(be.visible)

        return self

    @allure.step("Выполняем логин в UI")
    def login(self, username: str, password: str):
        browser.element("#userName").type(username)
        browser.element("#password").type(password)
        browser.element("#login").click()
        return self

    @allure.step("Проверяем, что пользователь '{username}' успешно авторизован")
    def should_be_logged_in_as(self, username: str):
        browser.element("#userName-value").should(have.text(username))