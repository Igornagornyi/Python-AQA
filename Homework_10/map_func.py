from filter_func import list_elem


def add_element(callback: callable,
                sequence: list[str]) -> list[str]:
    """Add element 's' to str elements in the list"""
    my_list = []
    for item in sequence:
        my_list.append(''.join(item)+'s')

    return my_list


print(add_element(lambda item: item + 's', list_elem))
