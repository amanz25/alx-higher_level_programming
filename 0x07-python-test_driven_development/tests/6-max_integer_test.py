#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    # unit test to test the max integer
    def testfromMultipleDigits(self):
        self.assertEqual(max_integer([56,26,89,75], 89)

    def testusingsinglevalue(self):
        self.assertEqual(max_integer([25], 25)

    def testemptylist(self):
        self.assertEqual(max_integer([], None)

    def testpositiveandnegativevalues(self):
        self.assertEqual(max_integer([-1, 2, 0, -8], 2)

    def testonlynegativevalues(self):
        self.assertEqual(max_integer([-5, -6, -1, -10], -1)

if __name__ == '__main__':
    unittest.main()
