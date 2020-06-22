from .base_page import BasePage
import allure
from steps.elements import Elements

class LoginPage(BasePage, Elements):

    def login_true_log_pass(self):
        self.login_aututestuser("AutotestUser")
        self.send_password("AutotestUser123")
        assert self.log_icon_in_post().text == "AutotestUser", "User isn't authorized or not autotest user"


    def login_wrong_log(self):
        self.login_aututestuser("NoAutotestUser")
        self.error_notification()


    def login_wrong_pass(self):
        self.login_aututestuser("AutotestUser")
        self.send_password("NoAutotestUser123")
        self.error_notification()

    def login_aututestuser(self, log):
        self.button_log_click()
        self.send_login(log)

    def exit_autotestuser(self):
        self.log_icon_in_post().click()
        self.button_exit_from_post().click()
        assert self.button_create_post(), "You are login user"



    def check_buttons_over_search(self):
        self.check_buttons_all_on_search()

    def check_button_for_over_search(self):
        self.check_button_on_search('images')


    def change_language(self):
        self.button_change_language()
        self.button_more_change_language()
        self.select_lang_eng()
        with allure.step("at_page"):
            self.assert_lang('Eng')
