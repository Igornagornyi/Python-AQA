from tabulate import tabulate
def print_table():
    column_name = ['value', 'escape sequencies']
    value = [['\\a', 'Bell (alert)'], ['\\b', 'Backspace'],
                ['\\n', 'New line'], ['\\t', 'Horizontal tab'],
                ["\\", "Backslash \ "], ['\\"', 'Double quotation mark "'],
                    ["\\'",   "Single quotation mark '"]]

    return tabulate(value, column_name, tablefmt="grid")

print(print_table())