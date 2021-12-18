import unittest
from Homework_05 import homework_05
from Homework_05.homework_05 import names_str, \
      query_str, camel_case, friends_list


class CapitalNames(unittest.TestCase):

    def test_a(self):
        """Check given value is str"""
        out = homework_05.capital_names(value=names_str)
        self.assertIsInstance(out, str)

    def test_b(self):
        """Check all names with capitals"""
        out = homework_05.capital_names(value=names_str)
        result = out.split()
        for item in result:
            self.assertEqual(item[0], item[0].upper())


class PrintFriends(unittest.TestCase):

    def test_a(self):  # error
        """Check given value is str"""
        out = homework_05.print_friends(value=friends_list)
        self.assertIsInstance(out, list)

    def test_b(self):  # error
        """Check length of given value equal to 30"""
        self.assertEqual(len(friends_list), 5)


class CreateDict(unittest.TestCase):

    def test_a(self):
        """Check result is dict"""
        out = homework_05.create_dict(value=query_str)
        self.assertIsInstance(out, dict)

    def test_b(self):  # error
        """Check length of dict"""
        out = homework_05.create_dict(value=query_str)
        result = len(out)
        self.assertEqual(result, 6)


class CreateStr(unittest.TestCase):

    def test_a(self):
        """Check string in the list has '_' element"""
        out = homework_05.create_str(value=camel_case)
        for item in out:
            self.assertIn('_', item)

    def test_b(self):
        """Check all letters in string is lower"""
        out = homework_05.create_str(value=camel_case)
        for item in out:
            self.assertEqual(item, item.lower())


if __name__ == '__main__':
    unittest.main(verbosity=2)
