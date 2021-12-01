list = [3, 35, 97, 72, 19]


def add_operation(value, item):
    """Function summarizes two elements"""
    return value + item


function = add_operation


def implement_reduce_func(function,
                          value: int, List: int) -> int:
    """Function summarizes elements in the list with each other"""
    for item in List:
        value = function(value, item)
    return value


print(implement_reduce_func(function, value=0, List=list))
