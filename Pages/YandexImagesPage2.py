from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class YandexImagesPage2(object):
    firstLinkLocator = (By.CSS_SELECTOR, "div.PopularRequestList-Item_pos_0 div.PopularRequestList-SearchText")
    inputElementSearchLocator = (By.CSS_SELECTOR, "input.input__control")
    imagesLocator = (By.CSS_SELECTOR, "img.serp-item__thumb")
    waitTimeout = 5

    def __init__(self, driver):
        self.drv = driver
        self.waitVariable = WebDriverWait(self.drv, self.waitTimeout)
        self.inputElementSearch = self.waitVariable.until(expected_conditions.element_to_be_clickable(self.inputElementSearchLocator))
        self.inputElementSearchText = self.inputElementSearch.get_attribute('value')
        self.images = self.drv.find_elements(*self.imagesLocator)

    def get_input_element_search(self):
        return self.inputElementSearch

    def get_input_element_search_text(self):
        return self.inputElementSearchText

    def get_images(self):
        return self.images
