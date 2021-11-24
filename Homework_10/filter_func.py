import string
import random


# Create two lists with random str elements
list1 = [random.choices(string.ascii_letters,
         k=random.randint(1, 5)) for i in range(50)]
list2 = [random.choices(string.ascii_letters,
         k=random.randint(1, 5)) for i in range(50)]


def find_common_elem(list1: list, list2: list) -> list[list] | str:
    """Find common elements in both lists"""
    result = list(filter(lambda i: i in list1, list2))
    if result:
        return f"Вот общие элементы: {result}"
    else:
        return 'Спробуй ще'


print(find_common_elem(list1, list2))
