import unittest
            
from src.AoC2018.day05.day05 import *


class TestPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(part1("dabAcCaCBAcCcaDA"), 10)
    def test1(self):
        self.assertEqual(part1("FuUmMfRbBVvYyzZrzZuUoffhNnHjAkAaiIvVKUumNnMtTa"), 4)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(), None)