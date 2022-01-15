import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from MainPage import MainPage
from SearchPage import SearchPage


class Main(unittest.TestCase):
    seleniumWebDriverPath = r"C:\app\selenium\webdriver\chromedriver.exe"
    urlForTest = "https://yandex.ru"
    stringForSearch = "Тензор"
    linksUrl = "tensor.ru"
    title = "Яндекс"

    ser = Service(r"C:\app\selenium\webdriver\chromedriver.exe")
    opt = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=ser, options=opt)
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(self):
        self.driver.get(self.urlForTest)
        self.mp = MainPage(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test1_if_its_yandex(self):
        self.assertTrue(self.title in self.mp.get_title())

    def test2_if_search_input_exist(self):
        self.assertTrue(self.mp.get_inputElementSearch())

    def test3_if_suggestions_exist(self):
        if self.mp.get_inputElementSearch():
            self.mp.get_inputElementSearch().send_keys(self.stringForSearch)
            self.assertTrue(self.mp.get_suggestions())

    def test4_if_all_5_fist_search_result_have_link(self):
        self.mp.get_inputElementSearch().submit()
        self.sp = SearchPage(self.driver)
        searchResultLinks = self.sp.get_searchResultLinks()
        i = 0
        for searchResultLink in searchResultLinks[:5]:
            s = searchResultLink.get_attribute("href")
            if self.linksUrl in s:
                i += 1
        self.assertEqual(i, 5)


if __name__ == "__main__":
    unittest.main()
