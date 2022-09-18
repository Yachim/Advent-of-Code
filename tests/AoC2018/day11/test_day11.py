import unittest
            
from src.AoC2018.day11.day11 import *

class TestGetPowerLeve(unittest.TestCase):
    def test(self):
        self.assertEqual(get_power_level(3, 5, 8), 4)
        
class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(18), "33,45")
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(18), "90,269,16")