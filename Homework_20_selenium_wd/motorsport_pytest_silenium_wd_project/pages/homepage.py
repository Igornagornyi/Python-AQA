from .basepage import Basepage
from .newspage import Newspage


class Homepage(Basepage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__news_button_locator = \
            "//ul[@class='ms-content-menu visible']//a[@href='/all/news/']"
        self.__subscribe_button_locator = \
            "//div[@class='ms-footer_top-start']//a[contains(text(), 'Subscribe to our newsletter')]"

    def check_subscribe_item_title(self) -> str:
        self._scroll_to_the_element(self.__subscribe_button_locator)
        return self._driver.find_element_by_xpath(self.__subscribe_button_locator).text

    def select_news(self) -> Newspage:
        self._click_on_element(self.__news_button_locator)
        return Newspage(self._driver)
