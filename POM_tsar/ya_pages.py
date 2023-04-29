from selenium.webdriver.common.by import By
# класс By, содержит определения разных типов поиска. Далее мы внутри класса
# определяем локаторы в виде списка с типом поиска и поисковой фразой
# (строкой локатора).

from .base_page import BasePage

class YaSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Найти')]")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_search_button(self):
        return self.find_element\
            (YaSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

