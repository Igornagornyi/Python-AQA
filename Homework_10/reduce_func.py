from filter_func import list_elem
from typing import List


def convert_str_to_int(sequence: List[str]) -> int:
    """Function converts str elem to int"""
    str_list = []
    int_list = []
    for item in sequence:
        str_list.append(''.join(item))
    for item in str_list:
        int_list.append((len(item)))

    return int_list


function = convert_str_to_int(list_elem)


def add_operation(initial_value, item):
    """Function summarizes two elements"""
    return initial_value + item


def implement_reduce_func(add_operation,
                          initial_value: int, List: int) -> int:
    """Function summarizes elements in the list with each other"""
    for item in List:
        initial_value = add_operation(initial_value, item)
    return initial_value


print(implement_reduce_func(add_operation, initial_value=0, List=function))
