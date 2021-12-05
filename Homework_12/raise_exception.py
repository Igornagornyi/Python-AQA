from typing import List


def check__quantiy_elements(int_list: int) -> List[int] | str:
    """Raise exception if length > 10"""
    while len(int_list) < 10:
        value = int(input('Введите число: '))
        int_list.append(value)

    else:
        print(int_list)
        raise Exception('You have already added 10 elements')


check__quantiy_elements([2, 4, 7, 8, 3])
