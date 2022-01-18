from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


driver = Chrome("./chromedriver")
driver.get("https://www.motorsport.com/")
driver.maximize_window()
news_button: WebElement = driver.find_element(
    By.XPATH,
    "//ul[@class='ms-content-menu visible']//a[@href='/all/news/']")
sleep(5)
news_button.click()
sleep(5)
filter_button: WebElement = driver.find_element(
    By.XPATH,
    "//div[@class='ms-filter_toggler']")
filter_button.click()
sleep(5)
search_field: WebElement = driver.find_element(
    By.XPATH,
    "//input[@class='ms-filter-search_input']")
search_field.send_keys("Formula")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.ScrollTop)")
sleep(5)
driver.quit()
