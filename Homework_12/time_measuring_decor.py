import time
from typing import List


def time_decor(function) -> str:
    """Calculate time of operation"""
    def decoratee(number):
        start_point = time.time()
        function(number)
        time_operating = time.time() - start_point
        print(f"Время выполнения: {time_operating}")
    return decoratee


@time_decor
def raise_number(length: int) -> List[int]:
    """Raise to square all numbers from 0 to given int"""
    int_list = []
    counter = 0
    while counter < length:
        counter += 1
        int_list.append(counter**2)
    print(int_list)
    

if __name__ == '__main__':
    
    raise_number(10000)
