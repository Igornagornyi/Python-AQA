list = [3, 35, 97, 72, 19]


def sum_operation(value, item):
    """Function summarizes two elements"""
    return value + item


def implement_reduce_func(sum_operation,
                          value: int, List: int) -> int:
    """Function summarizes elements in the list with each other"""
    for item in List:
        value = sum_operation(value, item)
    return value


print(implement_reduce_func(sum_operation, value=0, List=list))
