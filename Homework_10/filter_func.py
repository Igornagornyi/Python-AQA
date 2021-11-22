def find_common_elem(list1: str, list2: str) -> list[str]:
    """Find common elements in both lists"""
    result = list(filter(lambda i: i in list1, list2))
    return f'Вот общие элементы: {result}'


list1 = ['rr', 'nn', 'mk', '/23']
list2 = ['vv', '23', 'mk', 'qw']
print(find_common_elem(list1, list2))
