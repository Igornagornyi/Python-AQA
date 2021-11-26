def raise_a_number(length: int) -> int:
    """Raise to square all even numbers from 0 to given int"""
    counter = 0
    while counter < length:
        counter += 1
        yield counter**2 if counter % 2 == 0 else counter


def show_numbers(number: int):
    for counter in raise_a_number(number):
        print(counter)


nn = show_numbers(100)
print(nn)
