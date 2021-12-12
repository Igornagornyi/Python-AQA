import calendar
import datetime
from typing import List


def show_dates() -> List[str]:
    """Show list of even dates"""
    dates_list = []
    today = datetime.date.today()
    quantity = calendar.monthrange(today.year, today.month)[1]
    counter = 1
    while counter <= quantity:
        date = datetime.date(today.year, today.month, counter)
        format_date = date.strftime("%d %B %Y")
        dates_list.append(format_date) if counter % 2 == 0 else None
        counter += 1

    return f"Список четных дат на текущий месяц: {dates_list}"


if __name__ == '__main__':

    print(show_dates())
