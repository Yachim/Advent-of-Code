import unittest
            
from src.AoC2018.day14.day14 import *

        
class TestPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(part1(5), "0124515891")
    def test2(self):
        self.assertEqual(part1(2018), "5941429882")
        
class TestPart2(unittest.TestCase):
    def test1(self):
        self.assertEqual(part2(51589), 9)
    def test2(self):
        self.assertEqual(part2(92510), 18)
    def test3(self):
        self.assertEqual(part2(59414), 2018)