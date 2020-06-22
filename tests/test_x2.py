from pages.base_page import BasePage
from pages.login_page_yandex import LoginPage
import pytest


@pytest.mark.ui
def test_correct_login(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_true_log_pass()

@pytest.mark.ui
def test_incorrect_login_l(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_wrong_log()

@pytest.mark.ui
def test_incorrect_login_p(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_wrong_pass()
