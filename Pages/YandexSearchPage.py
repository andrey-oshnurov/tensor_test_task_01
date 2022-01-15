from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class YandexSearchPage(object):
    url = "https://yandex.ru"
    inputElementSearchLocator = (By.XPATH, ".//input[@id='text']")
    suggestionLocator = (By.CLASS_NAME, "mini-suggest__item")

    def __init__(self, driver):
        self.drv = driver

    def load(self):
        self.drv.get(self.url)

    def get_title(self):
        self.title = self.drv.title
        return self.title

    def get_inputElementSearch(self):
        try:
            self.inputElementSearch = self.drv.find_element(*self.inputElementSearchLocator)
            return self.inputElementSearch
        except NoSuchElementException:
            return False

    def get_suggestions(self):
        return self.drv.find_elements(*self.suggestionLocator)