from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def check_exists_by_xpath(xpath):
    return len(driver.find_elements(By.XPATH, xpath)) > 0


def check_sugesstion_exists(suggestionsClassName):
    return len(driver.find_elements(By.CLASS_NAME, suggestionsClassName)) > 0


driver = webdriver.Chrome(executable_path="C:\\app\\selenium\\webdriver\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\app\\selenium\\webdriver\\geckodriver.exe")
url = "https://yandex.ru/"
xpath = ".//input[@id='text']"
stringForSearch = "Тензор"
suggestionsclassName = "mini-suggest__item"

try:
    driver.get(url=url)

    if check_exists_by_xpath(xpath):
        driver.implicitly_wait(5)
        print("Search Input was found")
        inputElement = driver.find_element(By.XPATH, xpath)
        inputElement.send_keys(stringForSearch)
        if check_sugesstion_exists(suggestionsclassName):
            print("Suggestions were found")
        else:
            print("Suggestions were not found")
        inputElement.send_keys(Keys.ENTER)

        #time.sleep(5)

        searchResultsText = driver.find_elements(By.CSS_SELECTOR, ".organic__url")
        i = 0
        for searchResultText in searchResultsText[:5]:
            s = searchResultText.get_attribute("href")
            if "tensor.ru" in s:
                i += 1
        if i < 5:
            print("All first 5 results do not contain a link to tensor.ru")
        elif i == 5:
            print("All first 5 results contain a link to tensor.ru")

    else:
        print("Error: Search Input was not found on page " + url)


except Exception as exc:
    print(exc)

finally:
    driver.close()
    driver.quit()
