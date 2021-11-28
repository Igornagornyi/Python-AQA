from filter_func import list_elem


def implement_map_func(callback: callable,
                       sequence: list[str]) -> list[str]:
    """Add element 's' to str elements in the list"""
    my_list = []
    for item in sequence:
        my_list.append(''.join(item)+'s')

    return my_list


print(implement_map_func(lambda item: item + 's', list_elem))
