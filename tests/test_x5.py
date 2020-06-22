from pages.base_page import BasePage
from pages.login_page_yandex import LoginPage
import allure
import pytest



class TestChangeLang:

    @allure.title("Create issue UI")
    @pytest.mark.xfail
    def test_change_language(self, browser):
        link = "https://yandex.by/"
        page = BasePage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.change_language()

