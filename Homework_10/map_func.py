def add_element_to_str(my_list: str | int) -> list[str]:
    """Add element 's' to every element in the list"""
    result = list(map(lambda i: str(i) + 's', my_list))
    return result


my_list = [45, 'hh', 'rr', 678]
print(add_element_to_str(my_list))
