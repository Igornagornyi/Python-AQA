from filter_func import list1, list2


def sort_dic_by_keys(list1: str, list2: str) -> list[tuple]:
    """Sort by length of dictionary keys"""
    list_str1 = list(map(lambda i: ''.join(i), list1))
    list_str2 = list(map(lambda i: ''.join(i), list2))
    my_dict = dict(zip(list_str1, list_str2))
    return sorted(my_dict.items(), key=lambda i: len(i[0]), reverse=True)


print(sort_dic_by_keys(list1, list2))
