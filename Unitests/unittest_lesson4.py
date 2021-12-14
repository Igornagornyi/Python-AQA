import unittest
from Homework_04.homework_04 import print_table, column_name, value


check_value = [['\\a', 'Bell (alert)'], ['\\b', 'Backspace'],
               ['\\n', 'New line'], ['\\t', 'Horizontal tab'],
               ["\\", "Backslash \ "], ['\\"', 'Double quotation mark "']]


class CheckTable(unittest.TestCase):

    def test_a(self):  # error
        """Check horizontal element in escape sequence table"""
        out = print_table(column_name, check_value)
        exp = print_table(column_name, value)
        self.assertEqual(out, exp)

    def test_b(self):
        """Check vertical element in escape sequence table"""
        out = 'escape sequencies'
        exp = column_name
        self.assertIn(out, exp)


if __name__ == '__main__':
    unittest.main(verbosity=2)
