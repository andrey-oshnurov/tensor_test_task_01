from selenium.webdriver.common.by import By


class YandexImagesPage3(object):
    imageLocator = (By.CSS_SELECTOR, "img.MMImage-Origin")
    buttonNextLocator = (By.CSS_SELECTOR, "div.CircleButton_type_next")
    buttonPrevLocator = (By.CSS_SELECTOR, "div.CircleButton_type_prev")

    def __init__(self, driver):
        self.drv = driver

    def check_if_exist_img(self):
        return len(self.drv.find_elements(*self.imageLocator)) > 0

    def get_image_url(self):
        return self.drv.find_elements(*self.imageLocator)[0].get_attribute('src')

    def get_next_button(self):
        return self.drv.find_elements(*self.buttonNextLocator)[0]

    def get_prev_button(self):
        return self.drv.find_elements(*self.buttonPrevLocator)[0]
