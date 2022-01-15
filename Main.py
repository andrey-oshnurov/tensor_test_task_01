import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Main(unittest.TestCase):
    seleniumWebDriverPath = r"C:\app\selenium\webdriver\chromedriver.exe"
    urlForTest = "https://yandex.ru"
    searchInputXpath = ".//input[@id='text']"
    stringForSearch = "Тензор"
    linksUrl = "tensor.ru"
    suggestionsClassName = "mini-suggest__item"
    searchResultLinksCssSelector = ".organic__url"
    title = "Яндекс"

    ser = Service(r"C:\app\selenium\webdriver\chromedriver.exe")
    opt = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=ser, options=opt)
    driver.implicitly_wait(5)


    @classmethod
    def setUpClass(self):
        # print("Open Browser Window")
        # print(".", end='')
        self.driver.get(self.urlForTest)

    @classmethod
    def tearDownClass(self):
        # print("Close Browser Window")
        # print(".", end='')
        self.driver.close()

    def test1_if_its_yandex(self):
        self.assertTrue(self.title in self.driver.title)

    def test2_if_search_input_exist(self):
        self.assertTrue(len(self.driver.find_elements(By.XPATH, self.searchInputXpath)) > 0)

    def test3_if_suggestions_exist(self):
        if len(self.driver.find_elements(By.XPATH, self.searchInputXpath)) > 0:
            inputElement = self.driver.find_element(By.XPATH, self.searchInputXpath)
            inputElement.send_keys(self.stringForSearch)
            self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, self.suggestionsClassName)) > 0)

    def test4_if_all_5_fist_search_result_have_link(self):
        inputElement = self.driver.find_element(By.XPATH, self.searchInputXpath)
        inputElement.submit()
        searchResultsText = self.driver.find_elements(By.CSS_SELECTOR, self.searchResultLinksCssSelector)
        i = 0
        for searchResultText in searchResultsText[:5]:
            s = searchResultText.get_attribute("href")
            if self.linksUrl in s:
                i += 1
        self.assertEqual(i, 5)


if __name__ == "__main__":
    unittest.main()
