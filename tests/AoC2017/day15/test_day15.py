from concurrent.futures import process
import unittest

from src.AoC2017.day15.day15 import *

TEST_INPUT = """Generator A starts with 65
Generator B starts with 8921"""

class TestInputProcessing(unittest.TestCase):
    def test1(self):
        inp = """Generator A starts with 116
Generator B starts with 299"""

        self.assertEqual(process_input(inp), {"A": 116, "B": 299})

    def test2(self):
        self.assertEqual(process_input(TEST_INPUT), {"A": 65, "B": 8921})

class TestNewValCalculation(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculate_val("A", 65), 1092455)

    def test2(self):
        self.assertEqual(calculate_val("B", 8921), 430625591)

class TestValMatch(unittest.TestCase):
    def test1(self):
        self.assertFalse(matches(1092455, 430625591))

    def test2(self):
        self.assertTrue(matches(245556042, 1431495498))

class TestSolve(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solve(TEST_INPUT, 40000000), 588)

    def test_part2(self):
        self.assertEqual(solve(TEST_INPUT, 5000000, True), 309)