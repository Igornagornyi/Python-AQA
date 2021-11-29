import string
import random
from typing import List, Tuple


# Create two lists with random str elements
list_elem = [random.choices(string.ascii_letters,
             k=random.randint(1, 5)) for i in range(100)]


def implement_filter_func(function,
                          sequence: List[str]) -> Tuple[str]:
    """Find elements in the list which count > 1"""
    my_list = []
    for item in sequence:
        my_list.append(''.join(item))
        result = set(my_list)

    return result


print(implement_filter_func(lambda element:
                            list_elem.count(element) > 1, list_elem))
