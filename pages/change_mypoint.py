from .base_page import BasePage
from steps.elements import Elements

class ChangePage(BasePage, Elements):

    def london_paris(self):
        self.send_london()
        London = self.city_more()
        self.send_paris()
        Paris = self.city_more()
        assert London == Paris, "More is different"


    def send_london(self):
        self.my_place()
        self.send_myplace("Londo")
        self.after_my_place()
        assert self.my_geolink().text == "Лондон", "You'r geolink isn't london"


    def send_paris(self):
        self.my_place()
        self.send_myplace("Pari")
        self.after_my_place()
        assert self.my_geolink().text == "Париж", "You'r geolink isn't Paris"


    def my_place(self):
        assert self.my_geolink(), "Button 'geolink' is not found"
        self.my_geolink().click()


    def after_my_place(self):
        self.first_in_list()
        self.check_b_more()
        self.button_more().click()


