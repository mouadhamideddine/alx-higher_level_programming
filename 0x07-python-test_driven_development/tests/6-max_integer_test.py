#!/usr/bin/python3
""" Test for max_integer module """
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):

    def test_empty_list(self):
        result1 = max_integer([])
        self.assertEqual(result1, None)
    # def test_string_list(self):
        # self.assertRaises(Exception, max_integer, ["777", "string", "string"])
    def test_unsigned_list_of_ints(self):
        result2 = max_integer([1, 2, 3, 7000, 0])
        self.assertEqual(result2, 7000)

if __name__ == '__main__':
    unittest.main()
