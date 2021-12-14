import unittest
from Homework_05.homework_05 import capital_names, names_str, print_friends, friends_list


class CapitalNames(unittest.TestCase):

    def test_a(self):
        out = capital_names(value=names_str)
        self.assertIsInstance(out, str)

    def test_b(self):
        out = capital_names(value=names_str)
        result = out.split()
        for item in result:
            self.assertEqual(item[0], item[0].upper())


class PrintFriends(unittest.TestCase):

    def test_a(self):  # error
        out = print_friends(value=friends_list)
        self.assertIsInstance(out, str)

    def test_b(self):  # error
        self.assertEqual(len(friends_list), 30)



if __name__ == '__main__':
    unittest.main(verbosity=2)
