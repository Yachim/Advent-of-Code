import unittest

from src.AoC2018.day01.day01 import *

class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input("""1
        2
        3"""), [1,2,3])

class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(process_input("""1
        2
        3""")), 6)

class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(process_input("""+1
-1""")), 0)