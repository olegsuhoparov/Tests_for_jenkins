#from selenium.webdriver.support.ui import Select


class Actions():


    def keydown_enter(self, how, what):                                           # списочный костыль, 1 элемент в выпадающем поле после введении букв
        b = self.browser.find_element(how, what)
        import time
        from selenium.webdriver.common.keys import Keys
        time.sleep(0.5)
        b.send_keys(Keys.DOWN+Keys.ENTER)


    def get_text(self, how, what):
        b = self.browser.find_element(how, what).text
        return b


    def get_attr(self, how, what, witch):                                   # получить значение атрибута как текст
        b = self.browser.find_element(how, what).get_attribute(witch)
        return b


    def select_in_list(self, how, what, witch):                                   # выбрать из выпалающего списка элемент
        self.browser.find_element(how, what).select_by_value(witch)

    def send_file(self, how, what, witch):                                   # загрузить файл witch = 'text.txt'
        import os 

        current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
        file_path = os.path.join(current_dir, witch)           # добавляем к этому пути имя файла 
        element = self.browser.find_element(how, what).send_keys(file_path)
        return element

