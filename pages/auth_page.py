from .base_page import BasePage
from .locators import AuthLocators  # импорт локаторов
import time
from settings import *
import os

# Класс страницы авторизации: конструктор и методы
class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # os.getenv("LOGIN_URL") - берем переменную окружения установленную в
        # системе, если существует то используем её
        url = os.getenv("LOGIN_URL") or f"{BASE_URL}login"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(3)

    # Ввод эл.почты в элемент email
    def enter_email(self, value):
        self.email.send_keys(value)

    # Ввод пароля в элемент password
    def enter_pass(self, value):
        self.passw.send_keys(value)

    # Нажатие на кнопку "Войти"
    def btn_click(self):
        self.btn.click()




