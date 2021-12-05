def check__amount_elements():
    """Raise exception if length > 10"""
    int_list = [2, 4, 7, 8, 3]
    while len(int_list) < 10:
        value = input('Введите число: ')
        int_list.append(int(value))

    else:
        raise Exception('You have already added 10 elements')


check__amount_elements()
