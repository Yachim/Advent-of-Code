from pathlib import Path
import unittest

from src.AoC2017.day14.day14 import *

PATH = str(Path(__file__).parent.resolve())

class TestBinary(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(get_binary("a0c2017"), "1010000011000010000000010111")

class TestPart1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("flqrgnkx"), 8108)