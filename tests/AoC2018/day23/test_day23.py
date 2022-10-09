import unittest
            
from src.AoC2018.day23.day23 import *


class TestInputProcessing(unittest.TestCase):
    def test(self):
        with open("tests/AoC2018/day23/input.txt", "r") as f:
            self.assertEqual(process_input(f.read()), [
                ((0,0,0), 4),
                ((1,0,0), 1),
                ((4,0,0), 3),
                ((0,2,0), 1),
                ((0,5,0), 3),
                ((0,0,3), 1),
                ((1,1,1), 1),
                ((1,1,2), 1),
                ((1,3,1), 1)
            ])
        
class TestPart1(unittest.TestCase):
    def test(self):
        with open("tests/AoC2018/day23/input.txt", "r") as f:
            self.assertEqual(part1(process_input(f.read())), 7)
        
class TestPart2(unittest.TestCase):
    def test(self):
        with open("tests/AoC2018/day23/input2.txt", "r") as f:
            self.assertEqual(part2(process_input(f.read())), 36)