from filter_func import list_elem


def find_sum_items(callback: callable,
                   sequence: list[str]) -> int:
    """Find sum of length of items in the list"""
    str_list = []
    int_list = []
    for item in sequence:
        str_list.append(''.join(item))
    for element in str_list:
        int_list.append(len(element))
    result = sum(int_list)

    return result


print(find_sum_items(lambda item: sum(list_elem), list_elem))
