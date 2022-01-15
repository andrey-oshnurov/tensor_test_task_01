from selenium.webdriver.common.by import By


class MainPage(object):
    inputElementSearchXpath = ".//input[@id='text']"
    suggestionsClassName = "mini-suggest__item"

    def __init__(self, driver):
        self.drv = driver
        self.title = self.drv.title
        self.inputElementSearch = self.drv.find_element(By.XPATH, self.inputElementSearchXpath)

    def get_title(self):
        return self.title

    def get_inputElementSearch(self):
        return self.inputElementSearch

    def get_suggestions(self):
        return self.drv.find_elements(By.CLASS_NAME, self.suggestionsClassName)

