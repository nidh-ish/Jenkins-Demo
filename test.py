#!/usr/bin/python3

import unittest
from build import *

class SampleTest(unittest.TestCase):
    def test_addition(self):
        a = 7
        b = 3
        expected = 11
        self.assertEqual(addition(a, b), expected)
    def test_subtraction(self):
        a = 10
        b = 2
        expected = 8
        self.assertEqual(subtraction(a, b), expected)
    def test_multiplication(self):
        a = 10
        b = 12
        expected = 120
        self.assertEqual(multiplication(a, b), expected)
    def test_division(self):
        a = 14
        b = 2
        expected = 7
        self.assertEqual(division(a, b), expected)
    def test_mean(self):
        l = [1, 2, 3, 4, 5]
        expected = 3
        self.assertEqual(mean(l), expected)

if __name__ == '__main__':
    unittest.main()
