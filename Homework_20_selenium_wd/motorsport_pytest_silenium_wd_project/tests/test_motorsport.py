def test_check_subscribe_title_in_the_footer(homepage):
    assert "SUBSCRIBE TO OUR NEWSLETTER" == homepage.check_subscribe_item_title()


def test_check_search_result_on_newspage(homepage, newspage):
    homepage.select_news()
    assert "Formula" in newspage.get_search_result()
