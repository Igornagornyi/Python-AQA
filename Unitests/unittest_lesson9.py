from Homework_09.homework_09_1 import get_square_data
from Homework_09.homework_09_2 import arithmetic
import unittest
import os


class GetSquare(unittest.TestCase):

    def test_type(self):
        """Check type of output"""
        out = get_square_data(3)
        self.assertIsInstance(out, tuple)

    @unittest.expectedFailure
    def test_int(self):  # error
        """Check all items are int"""
        out = get_square_data(3)
        for item in out:
            self.assertIsInstance(item, int)

    def test_len(self):
        """Check len of float element equal to 5"""
        my_list = []
        out = get_square_data(3)
        my_list.append(str(out[2]))
        for i in my_list:
            my_list = list(i)
        self.assertEqual(len(my_list), 5)

    @unittest.skipIf(os.name != 'Windows', reason='Not supported')
    def test_len_float(self):
        """Check len of float element equal to 5"""
        my_list = []
        out = get_square_data(3)
        my_list.append(str(out[2]))
        for i in my_list:
            my_list = list(i)
        self.assertEqual(len(my_list), 5)


class Arithmetic(unittest.TestCase):

    def test_operation(self):
        """Check validation of unknown operation"""
        out = arithmetic(4, 2, '=')
        self.assertEqual(out, "Not known operation =")
        out = arithmetic(5, 4, '+')
        self.assertEqual(out, 9)
        out = arithmetic(5, 4, '/')
        self.assertTrue(out, float)

    @unittest.skip
    def test_skip_operation(self):
        """Check validation of unknown operation"""
        out = arithmetic(4, 2, '=')
        self.assertEqual(out, "Not known operation =")
        out = arithmetic(5, 4, '+')
        self.assertEqual(out, 9)
        out = arithmetic(5, 4, '/')
        self.assertTrue(out, float)


if __name__ == '__main__':
    unittest.main(verbosity=2)