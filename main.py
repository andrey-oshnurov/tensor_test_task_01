from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

log = ""

# Read the file passed as parameter as a properties file.
def load_properties(filepath, sep='=', comment_char='#'):
    props = {}
    with open(filepath, "rt", encoding="utf-8") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props


# Check if exist xpath
def check_exists_by_xpath(xpath):
    return len(driver.find_elements(By.XPATH, xpath)) > 0


# Check if exist suggestions
def check_sugesstion_exists(suggestionsClassName):
    return len(driver.find_elements(By.CLASS_NAME, suggestionsClassName)) > 0


props = load_properties("file.cfg")
ser = Service(props["SeleniumWebDriverPath"])
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=opt)

try:
    driver.get(url=props["urlForTest"])

    if check_exists_by_xpath(props["searchInputXpath"]):
        driver.implicitly_wait(5)
        log += "Search Input was found\n"
        inputElement = driver.find_element(By.XPATH, props["searchInputXpath"])
        inputElement.send_keys(props["stringForSearch"])
        if check_sugesstion_exists(props["suggestionsClassName"]):
            log += "Suggestions were found\n"
        else:
            log += "Suggestions were not found\n"
        inputElement.send_keys(Keys.ENTER)

        searchResultsText = driver.find_elements(By.CSS_SELECTOR, props["searchResultLinksCssSelector"])
        i = 0
        for searchResultText in searchResultsText[:5]:
            s = searchResultText.get_attribute("href")
            if "tensor.ru" in s:
                i += 1
        if i < 5:
            log += "All first 5 results do not contain a link to tensor.ru\n"
        elif i == 5:
            log += "All first 5 results contain a link to tensor.ru\n"

    else:
        log += "Error: Search Input was not found on page " + urlForTest + "\n"

    f = open('result.log', 'w')
    f.write(log)


except Exception as exc:
    print(exc)

finally:
    driver.close()
    driver.quit()
