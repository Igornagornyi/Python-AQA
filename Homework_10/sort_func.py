from typing import List
import random
import string


list_elem = [random.choices(string.ascii_letters,
             k=random.randint(1, 5)) for i in range(50)]


def implement_sort_func(sequence: List[list]) -> List[list]:
    """Create list with str elements in desc order"""
    str_list = []
    order_list = []
    for item in sequence:
        str_list.append(item)
    while str_list:
        max_item = str_list.pop(str_list.index(max(str_list, key=len)))
        order_list.append(max_item)
    return order_list


print(implement_sort_func(list_elem))
