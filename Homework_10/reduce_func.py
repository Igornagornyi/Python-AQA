from filter_func import list1, list2
from functools import reduce


def find_max_value(list1: list, list2: list) -> list[str]:
    """Create lists with max length items"""
    list_str1 = reduce(lambda a, b: a if len(a) >= len(b) else b, list1)
    list_str2 = reduce(lambda a, b: a if len(a) >= len(b) else b, list2)

    return f"{list_str1}\n{list_str2}"


print(find_max_value(list1, list2))
