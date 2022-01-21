import pytest
from selenium.webdriver import Chrome
from .pages.newspage import Newspage
from .pages.homepage import Homepage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("./core/infrastructure/bin/chromedriver")
    driver.get("https://www.motorsport.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def homepage(driver):
    yield Homepage(driver)


@pytest.fixture(scope="session")
def newspage(driver):
    yield Newspage(driver)
