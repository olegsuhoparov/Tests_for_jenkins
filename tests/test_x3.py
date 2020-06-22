from pages.base_page import BasePage
from pages.login_page_yandex import LoginPage
import pytest


@pytest.mark.ui
def test_x3(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.check_buttons_over_search()

