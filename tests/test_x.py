from pages.change_mypoint import ChangePage
from pages.base_page import BasePage
import pytest
import allure


@pytest.mark.ui
@pytest.mark.task_1
@pytest.mark.screenshot_on_failure
def test_more_london_paris(browser):
    link = "https://yandex.by/"
    page = BasePage(browser, link)
    page.open()
    change_page = ChangePage(browser, browser.current_url)
    change_page.london_paris()
