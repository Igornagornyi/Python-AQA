from __future__ import annotations
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .singleton import Singleton


class Basepage(Singleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__wait = WebDriverWait(self._driver, 20)

    def _click_on_element(self, by: str) -> None:
        element = self.__wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, by)
            )
        )
        element.click()

    def _scroll_to_the_element(self, by: str) -> None:
        target = self._driver.find_element_by_xpath(by)
        return target.location_once_scrolled_into_view

    # def __wait_element(self, by: str) -> WebElement:
    #     return self.__wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, by)
    #         )
    #     )

