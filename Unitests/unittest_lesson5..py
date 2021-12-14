import unittest
from Homework_05.homework_05 import capital_names, names_str

check_str = "aaaaaa"


class NamesCapital(unittest.TestCase):

    def test_a(self):
        out = capital_names(value=check_str)
        exp = capital_names(value=names_str)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
