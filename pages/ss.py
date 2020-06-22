from .base_page import BasePage
from .locators import BasePageLocators
import time


class ss(BasePage):

    def sss(self):
        self.button_c(*BasePageLocators.GEOLINK)
        time.sleep(5)