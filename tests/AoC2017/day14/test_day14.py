from pathlib import Path
import unittest
from unittest.mock import patch

from src.AoC2017.day14.day14 import *

PATH = str(Path(__file__).parent.resolve())

class TestBinary(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(get_binary("a0c2017"), "1010000011000010000000010111")

class TestCellUpdate(unittest.TestCase):
    def test1(self):
        grid = [
            [True, True, False],
            [False, True, False],
            [False, False, True]
        ]
        update_cell(grid, 1, 1)

        self.assertEqual(grid, [
            [False, False, False],
            [False, False, False],
            [False, False, True]
        ])
    def test2(self):
        grid = [
            [True, True, False],
            [False, False, False],
            [False, True, True]
        ]
        update_cell(grid, 1, 1)

        self.assertEqual(grid, [
            [True, True, False],
            [False, False, False],
            [False, True, True]
        ])
    def test3(self):
        grid = [
            [True, True, False],
            [False, True, False],
            [False, True, True]
        ]
        update_cell(grid, 0, 1)

        self.assertEqual(grid, [
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ])

class TestPart1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("flqrgnkx"), 8108)

class TestPart2(unittest.TestCase):
    @patch("src.AoC2017.day14.day14.create_grid", return_value=[
        [True, True, False],
        [True, False, False],
        [False, False, True]
    ])
    def test_custom(self, mocked):
        self.assertEqual(part2(""), 2)

    def test_part2(self):
        self.assertEqual(part2("flqrgnkx"), 1242)