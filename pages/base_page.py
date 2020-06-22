import sys
sys.path.append('..')
from helpers.helpers import Helpers
sys.path.append('..')
from helpers.actions import Actions



class BasePage(Helpers, Actions):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def open(self):                                             
        self.browser.get(self.url)

