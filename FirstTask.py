import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pages.YandexResultPage import YandexResultPage
from Pages.YandexSearchPage import YandexSearchPage


class FirstTask(unittest.TestCase):
    title = "Яндекс"
    stringForSearch = "Тензор"
    linksUrl = "tensor.ru"
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
        self.driver.close()

    def test1_if_its_yandex(self):
        self.searchPage.load()
        self.assertTrue(self.title in self.searchPage.get_title()), "It is not Yandex.ru"

    def test2_if_search_input_exist(self):
        self.assertTrue(self.searchPage.get_inputElementSearch()), "Search Input was not found"

    def test3_if_suggestions_exist(self):
        if self.searchPage.get_inputElementSearch():
            self.searchPage.get_inputElementSearch().send_keys(self.stringForSearch)
        self.assertTrue(self.searchPage.get_suggestions()), "Suggestions was not found"

    def test4_if_all_fist_five_link_contain_tensor_ru(self):
        i = 0
        if self.searchPage.get_inputElementSearch():
            self.searchPage.get_inputElementSearch().clear()
            self.searchPage.get_inputElementSearch().send_keys(self.stringForSearch)
            self.searchPage.get_inputElementSearch().submit()
            self.resultPage = YandexResultPage(self.driver)
            searchResultLinks = self.resultPage.get_searchResultLinks()
            for searchResultLink in searchResultLinks[:5]:
                s = searchResultLink.get_attribute("href")
                if self.linksUrl in s:
                    i += 1
        self.assertEqual(i, 5), "found links less than 5"


if __name__ == "__main__":
    unittest.main()
