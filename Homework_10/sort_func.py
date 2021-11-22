my_keys = ['a', 'by', 'loo', 'z', 'c']
my_values = [1, '3', '10iu', 2, 'QQ']


def sort_dic_by_keys(my_keys: str, my_values: int | str) -> dict[str]:
    """Sort by length of dictionary keys"""
    my_dict = dict(zip(my_keys, my_values))
    return sorted(my_dict.keys(), key=len)


def sort_dict_by_values(my_keys: str, my_values: int | str) -> dict[str]:
    """Sort by length of dictionary values"""
    values_to_str = list(map(lambda i: str(i), my_values))
    my_dict = dict(zip(my_keys, values_to_str))
    return sorted(my_dict.values(), key=len)


g = sort_dic_by_keys(my_keys, my_values)
d = sort_dict_by_values(my_keys, my_values)
print(g)
print(d)
