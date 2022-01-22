from .basepage import Basepage
from time import sleep


class Newspage(Basepage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__filter_button = "//div[@class='ms-filter_toggler']"
        self.__search_field = "//input[@class='ms-filter-search_input']"
        self.__search_field_result = "//div[@class='ms-filter-option']/span[1]"

    def __search_field_write_text(self) -> None:
        self._click_on_element(self.__filter_button)
        element = self._driver.find_element_by_xpath(self.__search_field)
        element.send_keys("Formula 1")
        sleep(2)

    def get_search_result(self) -> str:
        self.__search_field_write_text()
        return self._driver.find_element_by_xpath(self.__search_field_result).text
