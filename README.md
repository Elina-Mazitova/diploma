# 🎓 Diploma Project: UI + API + Mobile Automated Testing

Автоматизированный тестовый проект, включающий UI‑тесты (Todoist), API‑тесты (DemoQA, DummyJSON, FakeStore) и Mobile‑тесты (Wikipedia на Android).  
Проект использует современный стек инструментов, интеграции с Jenkins, Allure Report, Allure TestOps и Telegram‑уведомлениями.

---


## 🛠 Стек технологий

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


## 🧩 Архитектура проекта

| Компонент | Технологии | Описание |
|----------|------------|----------|
| UI | Selene, Selenium | Page Object, тесты Todoist |
| API | Requests, Pydantic, JSON Schema | DemoQA, DummyJSON, FakeStore |
| Mobile | Appium, BrowserStack | Android‑тесты Wikipedia |
| CI/CD | Jenkins, Allure, Telegram | Полный пайплайн + уведомления |

## 📌 Покрытый функционал

Проект включает три направления автоматизации: **UI**, **API** и **Mobile**.  
Каждый блок покрывает ключевые пользовательские сценарии и бизнес‑логику тестируемых сервисов.

---
## 🖥️ UI (Todoist)

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
## 🔌 API (DemoQA, DummyJSON, FakeStore)

| API | Покрытие |
|-----|----------|
| 🧩 DemoQA | Создание пользователя; генерация токена; логин; JSON Schema; API → UI |
| 🛒 DummyJSON | Авторизация; товары (GET/POST/PUT/DELETE); схемы |
| 🏷️ FakeStore | Товары (GET/POST/PUT/DELETE); модели; схемы |

---

## 📱 Mobile (Wikipedia, Android)

| Раздел | Покрытый функционал |
|--------|----------------------|
| 🚀 Онбординг | Полное прохождение; пропуск; проверка отображения |
| ⚙️ Настройки | Добавление языка; локализации; работа на BrowserStack |
| 🔍 Поиск | Открытие поиска; ввод запроса; проверка результатов |

## ▶️ Запуск тестов

Тесты можно запускать по направлениям с помощью меток Pytest:

### UI
```bash
pytest -m ui
```
### API
```bash
pytest -m api
```
### Mobile
```bash
pytest -m mobile
```
Полный запуск:
```bash
pytest
```


## 🚀 Jenkins

**Job:**  
[Ссылка на jenkins джобу](https://jenkins.autotests.cloud/job/Elina-Mazitova_diploma/)

**Скриншот:**  
![1](images/01.png)

---

## 📊 Allure Report

**Ссылка на отчёт:**  
[Ссылка на отчет](https://jenkins.autotests.cloud/job/Elina-Mazitova_diploma/79/allure/)

**Скриншот дашборд:**  
![2](images/02.png)

---

## 🧪 Allure TestOps

**Проект:**  
[Ссылка на проект](https://allure.autotests.cloud/project/5133/test-cases?treeId=0)

**Скриншот overview:**  
![3](images/03.png)

**Ручные тесты (2 шт):**  
![4](images/04.png)

---

## 📬 Telegram уведомления

![5](images/05.png)

---

## 👤 Автор
<p align="center">
  Сделано с ❤️ для дипломного проекта  
  <br>
  <a href="https://github.com/Elina-Mazitova">GitHub Элины Мазитовой</a>
</p>

