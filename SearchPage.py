from selenium.webdriver.common.by import By

class SearchPage(object):
    searchResultLinksCssSelector = ".organic__url"

    def __init__(self, driver):
        self.drv = driver
        self.title = self.drv.title

    def get_searchResultLinks(self):
        return self.drv.find_elements(By.CSS_SELECTOR, self.searchResultLinksCssSelector)

