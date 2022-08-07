import unittest
            
from src.AoC2018.day02.day02 import *


class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input(
"""abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
        ), ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"])
        
class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), 12)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]), "fgij")