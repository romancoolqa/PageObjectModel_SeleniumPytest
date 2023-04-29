# перед запуском установить зависимости:
# pytest-selenium, pytest, selenium, urllib3
# (последние два могут уже быть включены в первый)
from pages.auth_page import AuthPage
from settings import *

def test_auth_page(selenium):
   ''' Тест успешной авторизации'''

   page = AuthPage(selenium)
   page.enter_email(valid_email)
   page.enter_pass(valid_password)
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() == '/all_pets', "login error"
   # Метод get_relative_link возвращает относительный путь до текущей
   # страницы (без домена).

   # time.sleep(5) #задержка для учебных целей
   page.driver.quit()