from tabulate import tabulate

column_name = ['value', 'escape sequencies']
value = [['\\a', 'Bell (alert)'], ['\\b', 'Backspace'],
               ['\\n', 'New line'], ['\\t', 'Horizontal tab'],
               ["\\", "Backslash \ "], ['\\"', 'Double quotation mark "'],
                ["\\'",   "Single quotation mark '"]]

print(tabulate(value, column_name, tablefmt="grid"))

