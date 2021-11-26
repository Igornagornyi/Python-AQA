def raise_a_number(length: int) -> int:
    """Raise to square all even numbers from 0 to given int"""
    counter = 0
    while counter < length:
        counter += 1
        yield counter**2 if counter % 2 == 0 else counter


cc = raise_a_number(1000000000)
for counter in cc:
    print(counter)
