def test_check_subscribe_title_in_the_footer(homepage):
    assert "SUBSCRIBE" in homepage.check_subscribe_item_title()


def test_check_search_result_on_newspage(newspage):
    assert "Formula" in newspage.get_search_result()
