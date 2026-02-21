import time
import allure
from selene import browser, have, be


class LoginPage:

    @allure.step("Открываем страницу логина через главную страницу DemoQA")
    def open(self):
        with allure.step("Открываем главную страницу"):
            browser.open("https://demoqa.com/")

        with allure.step("Скроллим вниз"):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with allure.step("Удаляем рекламу до полного исчезновения"):
            for _ in range(20):  # до 20 попыток очистки
                browser.execute_script("""
                    // Удаляем все iframes (реклама часто в них)
                    document.querySelectorAll('iframe').forEach(el => el.remove());

                    // Удаляем известные рекламные блоки
                    const ids = ['fixedban', 'adplus-anchor', 'google_ads_iframe'];
                    ids.forEach(id => {
                        const el = document.getElementById(id);
                        if (el) el.remove();
                    });

                    // Удаляем оверлеи с большим z-index
                    document.querySelectorAll('div').forEach(el => {
                        const z = window.getComputedStyle(el).zIndex;
                        if (z && parseInt(z) > 1000) el.remove();
                    });

                    // Нажимаем кнопки Close / ×
                    document.querySelectorAll("button, span").forEach(el => {
                        const text = el.innerText.toLowerCase();
                        if (text.includes("close") || text.includes("schließen") || text.includes("×")) {
                            try { el.click(); } catch(e) {}
                        }
                    });

                    // Скрываем footer
                    const footer = document.getElementsByTagName('footer')[0];
                    if (footer) footer.style.display = 'none';
                """)

                if len(browser.all("iframe")) == 0:
                    break

                browser.sleep(0.3)

        with allure.step("Переходим в Book Store Application"):
            card = browser.element("//h5[text()='Book Store Application']")
            card.should(be.visible)
            card.click()

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
