from functools import reduce


def find_max_value(my_list: int) -> int:
    """Subtract minimum value from maximum value in the list"""
    result = reduce(lambda a, b: a-b if a > b else b-a, my_list)

    return result


my_list = [1, 10, 60]
print(find_max_value(my_list))
