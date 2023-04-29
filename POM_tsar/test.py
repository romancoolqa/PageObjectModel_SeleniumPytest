from .ya_pages import SearchHelper
from .search_page import SearchPageHelper


def test_search(browser):
    ya_main_page = SearchHelper(browser)
    ya_search_page = SearchPageHelper(browser)
    ya_main_page.go_to_site()
    ya_main_page.enter_word("Privet")
    ya_main_page.click_on_search_button()
    elements = ya_search_page.check_navi_bar()
    assert "Картинки" and "Видео" in elements

