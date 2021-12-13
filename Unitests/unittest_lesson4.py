import unittest
from Homework_04.homework_04 import print_table, column_name, value


check_value = [['\\a', 'Bell (alert)'], ['\\b', 'Backspace'],
               ['\\n', 'New line'], ['\\t', 'Horizontal tab'],
               ["\\", "Backslash \ "], ['\\"', 'Double quotation mark "']]


class CheckValue(unittest.TestCase):
    """Check value in escape sequence table"""
    def test_a(self):
        out = print_table(column_name, value)
        exp = print_table(column_name, value)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
