from typing import List


def implement_reduce_func(callback: callable, items: List[int]) -> int:
    """Summarize elements in the list with each other"""
    result = items[0]
    for item in items[1:len(items)]:
        result = callback(result, item)
    return result


print(implement_reduce_func(lambda a, b: a + b, [3, 35, 97, 72, 19, 68]))
