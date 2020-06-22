from pages.base_page import BasePage
from pages.login_page_yandex import LoginPage
import pytest


@pytest.mark.ui
@pytest.mark.task_3
def test_more_london_paris(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_true_log_pass()
    login_page.exit_autotestuser()
