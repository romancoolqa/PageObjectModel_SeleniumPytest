import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from settings import valid_email, valid_password, BASE_URL


def test_show_my_pets():
    ''' Тест успешной авторизации через сверку
    нахождения на разных разделах сайта'''

    user = valid_email
    password = valid_password

    driver = webdriver.Chrome("../chromedriver.exe")
    driver.get(f"{BASE_URL}login")
    driver.find_element (By.XPATH, "//input[@id='email']").send_keys (user)
    driver.find_element (By.XPATH, "//input[@id='pass']").send_keys (password)
    driver.find_element (By.XPATH, "//button[contains(text(),'Войти')]").submit()
    assert driver.find_element (By.TAG_NAME, 'h1').text == "PetFriends"
    WebDriverWait (driver, 10).until (
       EC.element_to_be_clickable ((By.XPATH, "//a[contains(text(),'Мои питомцы')]"))).click ()
    time.sleep(1)  # Для учебных целей, задержка на 1 сек
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'


