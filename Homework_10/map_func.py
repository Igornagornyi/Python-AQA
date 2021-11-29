from filter_func import list_elem
from typing import List


def implement_map_func(callback: callable,
                       sequence: List[str]) -> List[str]:
    """Add element 's' to str elements in the list"""
    my_list = []
    for item in sequence:
        my_list.append(callback(''.join(item)))

    return my_list


print(implement_map_func(lambda item: item + 's', list_elem))
