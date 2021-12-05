import calendar


def show_dates():
    dates_list = []
    user_year = int(input('Введите год: '))
    user_month = int(input(' Введите месяц: '))
    quantity = (calendar.monthrange(user_year, user_month)[1])
    counter = 1
    while counter <= quantity:
        dates_list.append(counter) if counter % 2 == 0 else None
        counter += 1

    return dates_list


print(show_dates())
