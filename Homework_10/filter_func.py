from typing import List


list = [1, 3, 5, 7, 9, 100, 64, 32]


def implement_filter_func(callback: callable,
                          sequence: List[int]) -> int:
    """Find elements in the list which count > int"""
    my_list = []
    for item in list:
        if callback(item):
            my_list.append(item)

    return my_list


print(implement_filter_func(lambda item:
                            item % 2 == 1, list))
