from typing import List
import random
import string


list_elem = [random.choices(string.ascii_letters,
             k=random.randint(1, 5)) for i in range(50)]


def implement_map_func(callback: callable,
                       sequence: List[str]) -> List[str]:
    """Add element 's' to str elements in the list"""
    my_list = []
    for item in sequence:
        my_list.append(callback(''.join(item)))

    return my_list


print(implement_map_func(lambda item: item + 's', list_elem))
