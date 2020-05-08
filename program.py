"test for python factorial function"

import unittest
import math


def my_factorial(x):
    'uses positive integer'

    if not x:
        raise TypeError("invalid input, number  needed")
    if x < 0:
        raise ValueError('factorial is defined only for non negative ')

    return math.factorial(x)


class Testfactorial(unittest.TestCase):
    "class to test custom factorial function"

    def test_correct_param(self):
        "correct params"
        expected = 24
        test_data = 4

        self.assertEqual(math.factorial(test_data), expected)
        self.assertEqual(my_factorial(test_data), expected)



    def test_missing_param(self):
        "missing params"
        with self.assertRaises(TypeError):
            self.assertEqual(my_factorial(), True)

    def test_empty_param(self):
        "empty params"
        with self.assertRaises(TypeError):
            self.assertEqual(my_factorial(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(my_factorial(''), True)

    def test_wrong_param_type(self):
        "wrong params"
        with self.assertRaises(TypeError) as err:
            my_factorial()
        with self.assertRaises(ValueError) as err:
            my_factorial(-5)


if __name__ == '__main__':
    unittest.main()