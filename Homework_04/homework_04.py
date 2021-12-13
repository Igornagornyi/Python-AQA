from tabulate import tabulate



column_name = ['value', 'escape sequencies']
value = [['\\a', 'Bell (alert)'], ['\\b', 'Backspace'],
             ['\\n', 'New line'], ['\\t', 'Horizontal tab'],
             ["\\", "Backslash \ "], ['\\"', 'Double quotation mark "'],
             ["\\'",   "Single quotation mark '"]]


def print_table(column_name, value):

    return tabulate(value, column_name, tablefmt="grid")


if __name__ == '__main__':
    print(print_table(column_name=column_name, value=value))
