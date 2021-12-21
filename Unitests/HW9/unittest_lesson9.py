from Homework_09.homework_09_1 import get_square_data
from Homework_09.homework_09_2 import arithmetic
import unittest
import os
from first_logging import logger


class GetSquare(unittest.TestCase):

    def test_type(self):
        """Check type of output"""
        out = get_square_data(3)
        logger.info('checking info')
        self.assertIsInstance(out, tuple)
        logger.error('checking error')

    @unittest.expectedFailure
    def test_int(self):  # error
        """Check all items are int"""
        out = get_square_data(3)
        for item in out:
            self.assertIsInstance(item, int)

    def test_dot(self):
        """Check dot in str"""
        out = get_square_data(3)
        self.assertIn('.', str(out[2]))

    @unittest.skipIf(os.name != 'nt', reason='Not supported')
    def test_dot_in_str(self):
        """Check dot in str"""
        out = get_square_data(3)
        self.assertIn('.', str(out[2]))


class Arithmetic(unittest.TestCase):

    def test_operation(self):
        """Check validation of unknown operation"""
        out = arithmetic(4, 2, '=')
        self.assertEqual(out, "Not known operation =")
        logger.debug('*checking debug operation*')
        out = arithmetic(5, 4, '+')
        self.assertEqual(out, 9)
        out = arithmetic(5, 4, '/')
        self.assertIsInstance(out, float)

    @unittest.skip
    def test_skip_operation(self):
        """Check validation of unknown operation"""
        out = arithmetic(4, 2, '=')
        self.assertEqual(out, "Not known operation =")
        out = arithmetic(5, 4, '+')
        self.assertEqual(out, 9)
        out = arithmetic(5, 4, '/')
        self.assertIsInstance(out, float)


if __name__ == '__main__':
    unittest.main(verbosity=2)
