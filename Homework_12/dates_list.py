import calendar
from typing import List


def show_dates() -> List[str]:
    """Show list of even dates"""
    dates_list = []
    user_year = int(input('Введите год: '))
    user_month = int(input('\nВведите месяц: '))
    quantity = calendar.monthrange(user_year, user_month)[1]
    counter = 1
    while counter <= quantity:
        dates_list.append(str(counter) + '.' + str(user_month) +
                          '.' + str(user_year)) if counter % 2 == 0 \
                          else None
        counter += 1

    return f"Список четных дат на текущий месяц: {dates_list}"


print(show_dates())
