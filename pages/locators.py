from selenium.webdriver.common.by import By
# класс By, содержит определения разных типов поиска. Далее мы внутри класса
# определяем локаторы в виде списка с типом поиска и поисковой фразой
# (строкой локатора).

# класс локаторов веб-элементов
class AuthLocators:
    AUTH_EMAIL = (By.XPATH, "//input[@id='email']")
    AUTH_PASS = (By.XPATH, "//input[@id='pass']")
    AUTH_BTN = (By.XPATH, "//button[contains(text(),'Войти')]")


