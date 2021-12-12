import unittest
from Homework_04 import homework_04


class HomeworkTest(unittest.Testcase):
    def test_a(self):
        out = homework_04.tabulate(value, column_name, tablefmt="grid")