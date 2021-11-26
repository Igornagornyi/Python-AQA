from filter_func import list1, list2


def sort_items_by_length(list1: list, list2: list) -> list:
    """Find max length str elements in both lists"""
    list_str1 = []
    list_str2 = []
    list_pop1 = []
    list_pop2 = []
    for i in list1:
        list_str1.append(''.join(i))
    while list_str1:
        max_item1 = list_str1.pop(list_str1.index(max(list_str1, key=len)))
        list_pop1.append(max_item1)
    for i in list2:
        list_str2.append(''.join(i))
    while list_str2:
        max_item2 = list_str2.pop(list_str2.index(max(list_str2, key=len)))
        list_pop2.append(max_item2)

    return f"{list_pop1}\n{list_pop2}"


vv = sort_items_by_length(list1, list2)
print(vv)


def sorted_func(list1: list, list2: list) -> list:
    """Sort by length of items"""
    list_str1 = []
    list_str2 = []
    for i in list1:
        list_str1.append(''.join(i))
    reusult1 = sorted(list_str1, key=len, reverse=True)
    for i in list2:
        list_str2.append(''.join(i))
    result2 = sorted(list_str2, key=len, reverse=True)

    return f"{reusult1}\n{result2}"


print(sorted_func(list1, list2))
