from selenium.webdriver import Chrome


driver = Chrome("./chromedriver")
driver.get("http://w3school.com")
driver.quit()
