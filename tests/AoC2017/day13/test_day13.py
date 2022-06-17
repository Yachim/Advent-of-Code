from pathlib import Path
import unittest

from src.AoC2017.day13.day13 import *

PATH = str(Path(__file__).parent.resolve())

class TestInputProcessing(unittest.TestCase):
    def test_input_processing(self):
        with open(PATH + "/test_input.txt", "r") as f:
            res = process_input(f.read())
        self.assertEqual(res, {
            0: 3,
            1: 2, 
            4: 4, 
            6: 4
        })


class TestGetCurrentIndex(unittest.TestCase):
    def test_get_current_index_at_0_len_3(self):
        self.assertEqual(get_current_index(0, 3), 0)
        
    def test_get_current_index_at_1_len_3(self):
        self.assertEqual(get_current_index(1, 3), 1)
    
    def test_get_current_index_at_4_len_3(self):
        self.assertEqual(get_current_index(4, 3), 0)
        
    def test_get_current_index_at_5_len_3(self):
        self.assertEqual(get_current_index(5, 3), 1)

    def test_get_current_index_at_6_len_4(self):
        self.assertEqual(get_current_index(6, 4), 0)
        
    def test_get_current_index_at_12_len_6(self):
        self.assertEqual(get_current_index(12, 6), 2)
        
    def test_get_current_index_at_5_len_6(self):
        self.assertEqual(get_current_index(5, 6), 5)
        
    def test_get_current_index_at_15_len_6(self):
        self.assertEqual(get_current_index(15, 6), 5)

    def test_get_current_index_at_10_len_3(self):
        self.assertEqual(get_current_index(10, 3), 2)


class TestPart1(unittest.TestCase):
    def test_part1(self):
        with open(PATH + "/test_input.txt", "r") as f:
            input = process_input(f.read())

        self.assertEqual(part1(input), 24)

    def test_part1_one_line(self):
        with open(PATH + "/test_input.txt", "r") as f:
            input = process_input(f.read())

        self.assertEqual(part1_one_line(input), 24)

class TestPart2(unittest.TestCase):
    def test_part1(self):
        with open(PATH + "/test_input.txt", "r") as f:
            input = process_input(f.read())

        self.assertEqual(part2(input), 10)

if __name__ == "__main__":
    unittest.main()