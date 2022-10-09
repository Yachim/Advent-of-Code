import unittest
            
from src.AoC2018.day16.day16 import *

test_input = """Before: [1, 1, 0, 3]
3 0 2 0
After:  [0, 1, 0, 3]

Before: [1, 1, 1, 3]
5 2 1 1
After:  [1, 2, 1, 3]



2 2 3 3
2 0 3 2
2 2 1 0"""

test_input2 = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]



1 1 1 1"""

class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertListEqual(process_input(test_input), [
            [
                {
                    "before": [1, 1, 0, 3],
                    "instruction": [3, 0, 2, 0],
                    "after": [0, 1, 0, 3]
                },
                {
                    "before": [1, 1, 1, 3],
                    "instruction": [5, 2, 1, 1],
                    "after":  [1, 2, 1, 3]
                }
            ], 
            [
                [2, 2, 3, 3]
                [2, 0, 3, 2]
                [2, 2, 1, 0]
            ]
        ])
        
class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(process_input(test_input2)), 1)