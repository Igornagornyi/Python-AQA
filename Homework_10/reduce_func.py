from filter_func import list1, list2
from functools import reduce


def find_max_item(list1: list, list2: list) -> list:
    """Find max length item in the list"""
    my_list1 = []
    my_list2 = []
    for i in list1:
        my_list1.append(''.join(i))
    result1 = list(max(my_list1, key=len))
    for i in list2:
        my_list2.append(''.join(i))
    result2 = list(max(my_list2, key=len))

    return f"{result1}\n{result2}"


rr = find_max_item(list1, list2)
print(rr)


def reduce_func(list1: list, list2: list) -> list:
    """Create lists with max length items"""
    list_str1 = reduce(lambda a, b: a if len(a) >= len(b) else b, list1)
    list_str2 = reduce(lambda a, b: a if len(a) >= len(b) else b, list2)

    return f"{list_str1}\n{list_str2}"


print(reduce_func(list1, list2))
