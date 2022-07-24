import unittest

from src.AoC2017.day17.day17 import *

class TestNextIndex(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_next_index([0], 0, 3), 0)
    def test_2(self):
        self.assertEqual(get_next_index([0, 1], 1, 3), 0)
    def test_3(self):
        self.assertEqual(get_next_index([0, 2, 1], 1, 3), 1)
    def test_4(self):
        self.assertEqual(get_next_index([0, 2, 3, 1], 2, 3), 1)
    def test_5(self):
        self.assertEqual(get_next_index([0, 9, 5, 7, 2, 4, 3, 8, 6, 1], 1, 3), 4)

class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(3), 638)