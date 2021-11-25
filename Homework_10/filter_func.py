import string
import random


# Create two lists with random str elements
list1 = [random.choices(string.ascii_letters,
         k=random.randint(1, 5)) for i in range(50)]
list2 = [random.choices(string.ascii_letters,
         k=random.randint(1, 5)) for i in range(50)]


def find_common_elem(list1: list, list2: list) -> set[str]:
    """Find the same elements in both lists """
    my_list = []
    for i in list1:
        if i in list2:
            my_list.append(''.join(i))
        result = set(my_list)
    if result:

        return f"Вот общие элементы: {result}"
    else:

        return 'Cпробуй ще'








ff = find_common_elem(list1, list2)
print(ff)

#
def filter_func(list1: list, list2: list) -> set[str]:
    """Find common elements in both lists"""
    my_list = []
    result = list(filter(lambda i: i in list1, list2))
    for i in result:
        my_list.append(''.join(i))
        result = set(my_list)
    if result:

        return f"Вот общие элементы: {result}"
    else:

        return 'Спробуй ще'


print(filter_func(list1, list2))
