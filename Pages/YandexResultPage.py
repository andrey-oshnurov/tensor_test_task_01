from selenium.webdriver.common.by import By


class YandexResultPage(object):
    searchResultLinksLocator = (By.CSS_SELECTOR, ".organic__url")

    def __init__(self, driver):
        self.drv = driver

    def get_searchResultLinks(self):
        return self.drv.find_elements(*self.searchResultLinksLocator)
