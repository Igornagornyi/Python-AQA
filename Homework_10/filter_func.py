import string
import random


# Create two lists with random str elements
list_elem = [random.choices(string.ascii_letters,
             k=random.randint(1, 5)) for i in range(100)]


def find_common_elem(callback: callable,
                     sequence: list[str]) -> tuple[str]:
    """Find elements in the list which count > 1"""
    my_list = []
    for item in sequence:
        if callback(item):
            my_list.append(''.join(item))
        result = set(my_list)

    return result


print(find_common_elem(lambda element:
                       list_elem.count(element) > 1, list_elem))
