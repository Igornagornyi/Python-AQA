from filter_func import list_elem
from typing import List


def implement_map_func(function,
                       sequence: List[str]) -> List[str]:
    """Add element 's' to str elements in the list"""
    my_list = []
    for item in sequence:
        my_list.append(''.join(item))

    return my_list


print(implement_map_func(lambda item: item + 's', list_elem))
