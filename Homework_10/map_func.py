from filter_func import list1, list2


def add_element_to_str(list1: list, list2: list) -> list[str]:
    """Add element 's' to every element in the lists"""
    list_str1 = list(map(lambda i: ''.join(i) + 's', list1))
    list_str2 = list(map(lambda i: ''.join(i) + 's', list2))

    return f"{list_str1}\n{list_str2}"


print(add_element_to_str(list1, list2))
