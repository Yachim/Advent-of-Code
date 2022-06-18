from pathlib import Path
import unittest
from unittest import mock
from unittest.mock import Mock

from src.AoC2017.day10.day10 import *

PATH = str(Path(__file__).parent.resolve())



class TestInputProcessing(unittest.TestCase):
    def test_input_processing(self):
        with open(PATH + "/test_input.txt", "r") as f:
            res = process_input(f.read())
        
        self.assertEqual(res, (3, 4, 1, 5))


class TestAsciiConversion(unittest.TestCase):
    def test_ascii_conversion(self):
        self.assertEqual(ascii_conversion("1,2,3"), [49,44,50,44,51,17,31,73,47,23])


class TestDenseHash(unittest.TestCase):
    def test_dense_hash(self):
        self.assertEqual(create_dense_hash([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]), [64])


class TestHex(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(create_hex([64, 7, 255]), "4007ff")


class TestPart1(unittest.TestCase):
    def test_part1(self):
        with open(PATH + "/test_input.txt", "r") as f:
            input = process_input(f.read())
        
        self.assertEqual(part1(5, input), 12)


class TestPart2(unittest.TestCase):
    def test_part2_1(self):        
        self.assertEqual(part2(256, "1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")

    def test_part2_2(self):
        self.assertEqual(part2(256, "1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

    def test_part2_3(self):
        self.assertEqual(part2(256, ""), "a2582a3a0e66e6e86e3812dcb672a272")

    def test_part2_4(self):
        self.assertEqual(part2(256, "AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")