from .locators import LoginPageLocators, ExtraLocators
from .locators import BasePageLocators
import allure


class Elements:


    @allure.feature('click on button log')
    @allure.step
    def button_alp(self):
        self.browser.find_element(*LoginPageLocators.BUTTON_LOG).click()

    @allure.feature('Change lang')
    def button_create_post(self):
        return self.browser.find_element(*LoginPageLocators.CREATE_POST)

    def error_notification(self):
        assert self.is_element_present(*LoginPageLocators.WRONG_LOG_PASS), "wrong login or password"

    def button_log_click(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK_YA).click()

    def log_icon_in_post(self):
        return self.browser.find_element(*LoginPageLocators.USER_ICON)

    def button_exit_from_post(self):
        return self.browser.find_element(*LoginPageLocators.EXIT_MENU)

    def send_login(self, log):
        self.switch_window(2)
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(log)
        self.button_alp()

    @allure.feature('send password in this field')
    @allure.step
    def send_password(self, pas):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(pas)
        self.button_alp()



    #для mypoint
    @allure.step
    def button_more(self):
        return self.browser.find_element(*BasePageLocators.MORE)

    @allure.step
    def send_myplace(self, where):
        self.browser.find_element(*BasePageLocators.SET_CITY).clear()
        return self.browser.find_element(*BasePageLocators.SET_CITY).send_keys(where)

    @allure.step
    def my_geolink(self):
        return self.browser.find_element(*BasePageLocators.GEOLINK)

    @allure.step
    def city_more(self):
        return self.browser.find_element(*BasePageLocators.MORE_T).text

    @allure.step
    def first_in_list(self):
        self.is_not_element_present(*BasePageLocators.LINK_WAIT)
        self.keydown_enter(*BasePageLocators.SET_CITY)

    @allure.step
    def check_b_more(self):
        assert self.is_element_present(*BasePageLocators.MORE), "Button more isn't found"





    @allure.feature('check buttons')
    @allure.step
    def check_buttons_all_on_search(self):
        b = 0
        c = ['video', 'images', 'news', 'maps', 'market', 'translate', 'music']
        for i in ((ExtraLocators.VIDEO), (ExtraLocators.IMAGES), (ExtraLocators.NEWS), (ExtraLocators.MAPS), \
                  (ExtraLocators.MARKET), (ExtraLocators.TRANSLATE), (ExtraLocators.MUSIC)):
            self.browser.find_element(*i).click()
            self.switch_window(2)
            assert self.is_text_in_url(c[b]), f"you're not go {c[b]} page or link changed"
            self.switch_window(0)
            b += 1

    @allure.step
    def check_button_on_search(self, keys):
        c = {'video': (ExtraLocators.VIDEO), 'images': (ExtraLocators.IMAGES), 'news':(ExtraLocators.NEWS), \
            'maps': (ExtraLocators.MAPS), 'market': (ExtraLocators.MARKET), \
            'translate': (ExtraLocators.TRANSLATE), 'music': (ExtraLocators.MUSIC)}
        self.browser.find_element(*c[keys]).click()
        self.switch_window(2)
        assert keys in self.browser.current_url, "you're not go to page"
        self.switch_window(0)

# меняем язык на инглиш
    @allure.feature('Change lang')
    @allure.story('click button')
    @allure.severity('blocker')
    @allure.step
    def button_change_language(self):
        self.browser.find_element(*ExtraLocators.LANGS_CHANGE).click()

    @allure.step
    def button_more_change_language(self):
        self.browser.find_element(*ExtraLocators.LANGS_MORE).click()

    @allure.step
    def select_lang_eng(self):
        self.stale_reference(*ExtraLocators.SELECT_LANG, *ExtraLocators.LANG_ENG)
        self.browser.find_element(*ExtraLocators.LANG_SAVE).click()

    @allure.step
    def assert_lang(self, lang):
        assert self.browser.find_element(*ExtraLocators.LANGS_CHANGE).text == f"{lang}", 'language not ' f"{lang}"
