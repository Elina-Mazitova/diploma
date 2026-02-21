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

        with allure.step("Удаляем ВСЮ рекламу, баннеры и оверлеи"):
            for _ in range(25):
                browser.execute_script("""
                    document.querySelectorAll('iframe').forEach(el => el.remove());

                    const ids = ['fixedban', 'adplus-anchor', 'google_ads_iframe'];
                    ids.forEach(id => {
                        const el = document.getElementById(id);
                        if (el) el.remove();
                    });

                    document.querySelectorAll('div').forEach(el => {
                        const style = window.getComputedStyle(el);
                        const z = parseInt(style.zIndex);
                        if (z > 1000) el.remove();
                    });

                    document.querySelectorAll('*').forEach(el => {
                        const style = window.getComputedStyle(el);
                        const pos = style.position;
                        const z = parseInt(style.zIndex);
                        if ((pos === 'fixed' || pos === 'sticky') && z > 100) {
                            el.remove();
                        }
                    });

                    document.querySelectorAll("button, span").forEach(el => {
                        const text = el.innerText.toLowerCase();
                        if (text.includes("close") || text.includes("×") || text.includes("schließen")) {
                            try { el.click(); } catch(e) {}
                        }
                    });

                    const footer = document.getElementsByTagName('footer')[0];
                    if (footer) footer.style.display = 'none';
                """)

                if len(browser.all("iframe")) == 0:
                    break

                time.sleep(0.3)

        with allure.step("Переходим в Book Store Application"):
            card = browser.element("//h5[text()='Book Store Application']/ancestor::a")
            card.should(be.visible)

            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", card())

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
