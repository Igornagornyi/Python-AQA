from operator import add


def implement_reduce_func(callback: callable, value: int, List: int) -> int:
    """Summarize elements in the list with each other"""
    result = value
    for item in List:
        result = callback(result, item)
    return result


print(implement_reduce_func(add, 0, [3, 35, 97, 72, 19]))
