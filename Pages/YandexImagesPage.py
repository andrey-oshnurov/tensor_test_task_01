from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class YandexImagesPage(object):
    firstLinkLocator = (By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0 div.PopularRequestList-SearchText")
    waitTimeout = 5

    def __init__(self, driver):
        self.drv = driver
        self.currentUrl = self.drv.current_url
        self.waitVariable = WebDriverWait(self.drv, self.waitTimeout)
        self.firstLinkElement = self.waitVariable.until(expected_conditions.element_to_be_clickable(self.firstLinkLocator))
        self.firstLinkText = self.firstLinkElement.text

    def get_url(self):
        return self.currentUrl

    def click_first_link(self):
        print(self.firstLinkText)
        self.firstLinkElement.click

    def get_first_link_element(self):
        return self.firstLinkElement

    def get_first_link_text(self):
        return self.firstLinkText
