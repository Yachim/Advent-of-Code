import unittest
            
from src.AoC2018.day08.day08 import *

class TestNode(unittest.TestCase):
    node_D = None
    node_C = None
    node_B = None
    node_A = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.node_D = Node( 0, 1, [], [99])
        cls.node_C = Node( 1, 1, [cls.node_D], [2])
        cls.node_B = Node( 0, 3, [], [10, 11, 12])
        cls.node_A = Node( 2, 3, [cls.node_B, cls.node_C], [1, 1, 2])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.node_D = None
        cls.node_C = None
        cls.node_B = None
        cls.node_A = None

    def test_sum(self):
        self.assertEqual(self.node_A.sum(), 138)

    def test_val(self):
        self.assertEqual(self.node_A.get_val(), 66)

class TestInputProcessing(unittest.TestCase):
    def test(self):
        node_D = Node( 0, 1, [], [99])
        node_C = Node( 1, 1, [node_D], [2])
        node_B = Node( 0, 3, [], [10, 11, 12])
        node_A = Node( 2, 3, [node_B, node_C], [1, 1, 2])

        res = process_input("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
        self.assertEqual(res, node_A)
        
class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(process_input("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")), 138)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(), None)