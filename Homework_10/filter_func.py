import string
import random
from typing import List, Tuple


# Create list with random str elements
list_elem = [random.choices(string.ascii_letters,
             k=random.randint(1, 5)) for i in range(50)]


def implement_filter_func(callback: callable,
                          sequence: List[str]) -> Tuple[str]:
    """Find elements in the list which count > int"""
    my_list = []
    for item in sequence:
        count = sequence.count(item)
        if callback(count):
            my_list.append(item)
    for item in my_list:
        my_list = ''.join(item)

    return set(my_list)


print(implement_filter_func(lambda count:
                            count > 1, list_elem))
