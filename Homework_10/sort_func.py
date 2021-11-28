from filter_func import list_elem


def sort_items_by_length(callback: callable,
                         sequence: list[str]) -> list:
    """Create list with str elements in desc order"""
    str_list = []
    order_list = []
    for item in sequence:
        str_list.append(''.join(item))
    while str_list:
        max_item = str_list.pop(str_list.index(max(str_list, key=len)))
        order_list.append(max_item)
    return order_list


print(sort_items_by_length(lambda item: len(item), list_elem))
