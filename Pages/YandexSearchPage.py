from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class YandexSearchPage(object):
    url = "https://yandex.ru"
    inputElementSearchLocator = (By.XPATH, ".//input[@id='text']")
    suggestionLocator = (By.CLASS_NAME, "mini-suggest__item")
    serviceLinkImagesLocator = (By.XPATH, ".//a[@data-id='images']/div[@class='services-new__item-title']")

    def __init__(self, driver):
        self.drv = driver

    def load(self):
        self.drv.get(self.url)

    def get_title(self):
        self.title = self.drv.title
        return self.title

    def get_input_element_search(self):
        try:
            self.inputElementSearch = self.drv.find_element(*self.inputElementSearchLocator)
            return self.inputElementSearch
        except NoSuchElementException:
            return False

    def get_suggestions(self):
        return self.drv.find_elements(*self.suggestionLocator)

    def get_service_link_images(self):
        try:
            return self.drv.find_element(*self.serviceLinkImagesLocator)
        except NoSuchElementException:
            return False

    def click_images_link(self):
        self.drv.find_element(*self.serviceLinkImagesLocator).click()
