import unittest
            
from src.AoC2018.day03.day03 import *

TEST_INPUT = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input(TEST_INPUT), [{"id": 1, "left": 1, "top": 3, "w": 4, "h": 4}, {"id": 2, "left": 3, "top": 1, "w": 4, "h": 4}, {"id": 3, "left": 5, "top": 5, "w": 2, "h": 2}])
        
class TestGetCoords(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_coords(3, 2, 2, 2), {
            (3, 2),
            (4, 2),
            (3, 3),
            (4, 3),
        })

class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(process_input(TEST_INPUT)), 4)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(process_input(TEST_INPUT)), 3)