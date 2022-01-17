import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.YandexSearchPage import YandexSearchPage
from Pages.YandexImagesPage import YandexImagesPage
from Pages.YandexImagesPage2 import YandexImagesPage2
from Pages.YandexImagesPage3 import YandexImagesPage3


class SecondTask(unittest.TestCase):
    title = "Яндекс"
    imagePageUrl = "https://yandex.ru/images/"
    firstImageSrc = ''
    #secondImageSrc = ''
    #thirdImageSrc = ''
    seleniumWebDriverPath = r"C:\app\selenium\webdriver\chromedriver.exe"
    ser = Service(seleniumWebDriverPath)
    opt = webdriver.ChromeOptions()

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=self.ser, options=self.opt)
        self.driver.implicitly_wait(5)
        self.searchPage = YandexSearchPage(self.driver)

    @classmethod
    def tearDownClass(self):
        print("")
        self.driver.close()
        self.driver.quit()

    def test1_if_its_yandex(self):
        self.searchPage.load()
        self.assertTrue(self.title in self.searchPage.get_title()), "It is not Yandex.ru"

    def test2_if_service_link_images_exist(self):
        self.assertTrue(self.searchPage.get_service_link_images()), "Search Input was not found"

    def test3_if_navigation_correct(self):
        if self.searchPage.get_service_link_images():
            self.searchPage.click_images_link()
            self.driver.switch_to.window(self.driver.window_handles[1])
            imagesPage = YandexImagesPage(self.driver)
        self.assertTrue(self.imagePageUrl in imagesPage.get_url()), "imagesPage has wrong url"

    def test4_if_input_has_correct_text(self):
        imagesPage = YandexImagesPage(self.driver)
        linkText = imagesPage.get_first_link_text()
        imagesPage.get_first_link_element().click()
        imagesPage2 = YandexImagesPage2(self.driver)
        inputText = imagesPage2.get_input_element_search_text()
        self.assertEqual(inputText, linkText), "Search Input has wrong text"

    def test5_if_first_image_was_opened(self):
        imagesPage2 = YandexImagesPage2(self.driver)
        imagesPage2.get_images()[0].click()
        imagesPage3 = YandexImagesPage3(self.driver)
        self.assertTrue(imagesPage3.check_if_exist_img()), "Image didn't open"

    def test6_image_change_if_click_forward(self):
        global firstImageSrc
        imagesPage3 = YandexImagesPage3(self.driver)
        firstImageSrc = imagesPage3.get_image_url()
        imagesPage3.get_next_button().click()
        secondImageSrc = imagesPage3.get_image_url()
        self.assertNotEqual(firstImageSrc, secondImageSrc), "Image did not change"

    def test7_image_return_if_click_back(self):
        imagesPage3 = YandexImagesPage3(self.driver)
        imagesPage3.get_prev_button().click()
        thirdImageSrc = imagesPage3.get_image_url()
        self.assertEqual(firstImageSrc, thirdImageSrc), "Image is not same"


if __name__ == "__main__":
    unittest.main()
