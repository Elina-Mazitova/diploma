
<div align="center">

# 🎓 Diploma Project  
### UI • API • Mobile Automated Testing  

</div>

---

<h2 align="center">🛠 Стек технологий</h2>


| Технология | Описание |
|-----------|----------|
| ![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) | язык разработки |
| ![Pytest](https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest&logoColor=white) | тестовый фреймворк |
| ![Selene](https://img.shields.io/badge/Selene-Selenium%20Wrapper-lightgrey) | обёртка над Selenium |
| ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white) | автоматизация браузера |
| ![Appium](https://img.shields.io/badge/Appium-Mobile%20Automation-purple?logo=appium&logoColor=white) | мобильная автоматизация |
| ![BrowserStack](https://img.shields.io/badge/BrowserStack-Cloud%20Devices-lightgrey?logo=browserstack&logoColor=white) | облачные устройства |
| ![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-red) | API‑клиент |
| ![Pydantic](https://img.shields.io/badge/Pydantic-Models-blue) | модели запросов/ответов |
| ![JSON Schema](https://img.shields.io/badge/JSON_Schema-Validation-yellow) | валидация схем |
| ![Allure](https://img.shields.io/badge/Allure-Report-pink?logo=allure&logoColor=white) | отчёты |
| ![Allure TestOps](https://img.shields.io/badge/Allure_TestOps-TMS-purple?logo=allure&logoColor=white) | управление тестами |
| ![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red?logo=jenkins&logoColor=white) | CI/CD |
| ![Telegram Bot API](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white) | уведомления |

---

<h2 align="center"> 🧩 Архитектура проекта</h2>

| Компонент | Технологии | Описание |
|----------|------------|----------|
| UI | Selene, Selenium | Page Object, тесты Todoist |
| API | Requests, Pydantic, JSON Schema | DemoQA, DummyJSON, FakeStore |
| Mobile | Appium, BrowserStack | Android‑тесты Wikipedia |
| CI/CD | Jenkins, Allure, Telegram | Полный пайплайн + уведомления |

---

<h3 align="center">  🖥️ UI (Todoist)</h3>

<table>
<tr>
<td>

### Покрытый функционал

| Раздел | Описание |
|--------|----------|
| 🔐 Авторизация | Успешный вход; негативные проверки; сообщения об ошибках |
| 📁 Проекты | Создание проекта; проверка появления в списке |
| 📝 Задачи | Создание; создание с дедлайном; редактирование; удаление |

</td>
<td width="300" align="center">

<img src="images/07.gif" width="400" style="border-radius:0px;">

</td>
</tr>
</table>


---


<h3 align="center">  🔌 API (DemoQA, DummyJSON, FakeStore) </h3>

| API | Покрытие |
|-----|----------|
| 🧩 DemoQA | Создание пользователя; генерация токена; логин; JSON Schema; API → UI |
| 🛒 DummyJSON | Авторизация; товары (GET/POST/PUT/DELETE); схемы |
| 🏷️ FakeStore | Товары (GET/POST/PUT/DELETE); модели; схемы |


---


<h3 align="center">  📱 Mobile (Wikipedia, Android) </h3>
<table>
<tr>
<td>

| Раздел | Покрытый функционал |
|--------|----------------------|
| 🚀 Онбординг | Полное прохождение; пропуск; проверка отображения |
| ⚙️ Настройки | Добавление языка; локализации; работа на BrowserStack |
| 🔍 Поиск | Открытие поиска; ввод запроса; проверка результатов |
</td>
<td width="300" align="center">

<img src="images/08.gif" width="200" style="border-radius:0px;">

</td>
</tr>
</table>


---

<h2 align="center"> ▶️ Запуск тестов </h2>

| Тип тестов | Команда |
|-----------|---------|
| 🖥️ UI | `pytest -m ui` |
| 🔌 API | `pytest -m api` |
| 📱 Mobile | `pytest -m mobile` |
| 🔄 Все тесты | `pytest` |

---

<h2 align="center"> 🚀 Jenkins</h2>

**Job:**  
[Ссылка на jenkins джобу](https://jenkins.autotests.cloud/job/Elina-Mazitova_diploma/)

**Скриншот:**  
![1](images/01.png)

---

<h2 align="center">  📊 Allure Report</h2>

**Отчёт:**  
[Ссылка на отчет](https://jenkins.autotests.cloud/job/Elina-Mazitova_diploma/79/allure/)

**Скриншот дашборд:**  
![2](images/02.png)

---

<h2 align="center"> 🧪 Allure TestOps</h2>

**Проект:**  
[Ссылка на проект](https://allure.autotests.cloud/project/5133/test-cases?treeId=0)

**Скриншот overview:**  
![3](images/03.png)

**Ручные тесты (2 шт):**  
![4](images/04.png)

---

<h2 align="center"> 📬 Telegram уведомления</h2>

![5](images/05.png)


<p align="center">
  Сделано с 💜 для дипломного проекта QA Guru 
  <br>
  <a href="https://github.com/Elina-Mazitova">GitHub Элины Мазитовой</a>
</p>

