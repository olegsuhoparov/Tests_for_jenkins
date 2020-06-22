from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helpers():

    def is_element_present(self, how, what):                                                # обработка исключения (элемент не найден)
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_text_in_url(self, text):                                                # текст в урле
        try:
            WebDriverWait(self.browser, 1).until(EC.url_contains(text))
        except TimeoutException:
            return False

        return True

    def stale_reference(self, how1, what1, how2, what2):     # "как бы не открывается список элементов"
        try:
            import time
            for i in range(15):
                time.sleep(0.1)
                self.browser.find_element(how1, what1).click()
                b = self.browser.find_element(how2, what2)
                if b:
                    b.click()
                    break
        except NoSuchElementException:
            self.stale_reference(how1, what1, how2, what2)


    def is_time_element_present(self, how, what, timeout=4):                                   # Ждем появления элемента 4 секунды
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def switch_window(self, n=1):                                                               # переход на новое окно браузера (1-2)
        first_window = self.browser.window_handles[0]
        second_window = self.browser.window_handles[1]
        if n == 1:
            self.browser.switch_to.window(first_window)
        elif n == 2:
            self.browser.switch_to.window(second_window)
        elif n == 0:
            self.browser.switch_to.window(second_window)
            self.browser.close()
            self.browser.switch_to.window(first_window)


    def is_not_element_present(self, how, what, timeout=2):                                   # тест падает, если появляется элемент за 2 сек
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def sa_sa(self):                                   # тест падает, если появляется элемент за 2 сек
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))



    def is_disappeared(self, how, what, timeout=2):                                           # тест падает, если элемент не исчезнет через 2 сек
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()


    def scroll_page(self, how, what):                                                           # скролл до элемента (b - селектор)
        b = self.browser.find_element(how, what)
        self.browser.execute_script('return arguments[0].scrollIntoView(true);', b)


    def button_wc(self, how, what, timeout=4):
        button = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        button.click()

                                                                                 # ждем условие появления текста witch по локатору what
    def wait_if_element(self, how, what, witch, timeout=3):
        WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((how, what), witch))
