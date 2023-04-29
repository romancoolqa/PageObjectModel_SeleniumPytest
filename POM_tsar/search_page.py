from selenium.webdriver.common.by import  By
# класс By, содержит определения разных типов поиска. Далее мы внутри класса
# определяем локаторы в виде списка с типом поиска и поисковой фразой
# (строкой локатора).
from .base_page import BasePage

class YaSearchPageLocators:
    LOCATOR_YANDEX_NAVI_BAR = (By.CSS_SELECTOR, ".service__name")
    # LOCATOR_YANDEX_NAVI_BAR = (By.XPATH, "//span[@class='service__name']")


class SearchPageHelper(BasePage):
    def check_navi_bar(self):
        all_list = self.find_elements(YaSearchPageLocators.LOCATOR_YANDEX_NAVI_BAR)
        return [x.text for x in all_list]



