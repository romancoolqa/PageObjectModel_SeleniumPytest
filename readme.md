Реализация паттерна Page Object на Python - pytest + selenium.
-
Цель: изучение паттерна программирование (шаблон проектирования) Page Object на примере сайта соцсети [PetFriends](https://petfriends.skillfactory.ru/).

В папке *pages/* находятся программные объекты для работы с элементами веб-страницы. В папке *tests/* - тесты. <br>
В папке *POM_tsar/* - реализация паттерна Page Object по материалам статьи на [Хабр](https://habr.com/ru/post/472156/).

### Как запускать тесты:
1) Установить все зависимости:
В командной строке терминала (bash) набрать и выполнить: 
pip install -r requirements.txt
2) Скачать Selenium WebDriver: https://chromedriver.chromium.org/downloads (выбрать совместимую версию с вашим браузером Chrome).
3) Запуск тестов: <BR>
```python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> ~/chrome tests/*```<br> 
<br>Примеры запуска:<br>
```python -m pytest -v --driver Chrome --driver-path D:/chromedriver_win32/chromedriver.exe tests/test_auth_page.pyy```
---
☝️ Пароли спрятаны в файл .env (не выложен здесь). <BR>
Создать в директории проекта файл .env, в него записать: <BR> 
```
valid_email = "ваша учетная запись"
valid_password = "ваш пароль"
BASE_URL = 'https://petfriends.skillfactory.ru/' 
```