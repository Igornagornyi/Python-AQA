from filter_func import list1, list2


def add_element(list1: list, list2: list) -> list:
    """Add element 's' to str elements in the list"""
    my_list1 = []
    my_list2 = []
    for i in list1:
        my_list1.append(''.join(i)+'s')
    for q in list2:
        my_list2.append(''.join(q)+'s')

    return f"{my_list1}\n{my_list2}"


yy = add_element(list1, list2)
print(yy)


def map_func(list1: list, list2: list) -> list:
    """Add element 's' to every element in the lists"""
    list_str1 = list(map(lambda i: ''.join(i) + 's', list1))
    list_str2 = list(map(lambda i: ''.join(i) + 's', list2))

    return f"{list_str1}\n{list_str2}"


print(map_func(list1, list2))
