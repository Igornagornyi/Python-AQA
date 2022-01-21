from .basepage import Basepage


class Newspage(Basepage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__filter_button = "//div[@class='ms-filter_toggler']"
        self.__search_field = "//input[@class='ms-filter-search_input']"
        self.__search_field_result = "//div[@class='ms-filter-option']/span[1]"

    def click_on_filters_button(self) -> None:
        self._click_on_element(self.__filter_button)

    def search_field_write_text(self) -> None:
        element = self._driver.find_element_by_xpath(self.__search_field)
        element.send_keys("Formula")

    def get_search_result(self) -> str:
        return self._driver.find_element_by_xpath(self.__search_field_result).text
