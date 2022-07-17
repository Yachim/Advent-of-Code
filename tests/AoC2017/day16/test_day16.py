import unittest
from unittest import mock

import numpy as np

from src.AoC2017.day16.day16 import *

class TestInputProcessing(unittest.TestCase):
    def test_elem_processing1(self):
        self.assertEqual(process_elem("s1"), {
            "type": "s",
            "size": 1
        })
    def test_elem_processing2(self):
        self.assertEqual(process_elem("x3/4"), {
            "type": "x",
            "first": 3,
            "second": 4
        })
    def test_elem_processing3(self):
        self.assertEqual(process_elem("pe/b"), {
            "type": "p",
            "first": "e",
            "second": "b"
        })
    def test_elem_processing4(self):
        with self.assertRaises(ValueError) as cmd:
            process_elem("q123")
        self.assertEqual(cmd.exception.args[0], "Invalid type")
    def test_input_processing(self):
        self.assertEqual(list(process_input("x5/15,s15,x1/3")), [
            {
                "type": "x",
                "first": 5,
                "second": 15
            },
            {
                "type": "s",
                "size": 15
            },
            {
                "type": "x",
                "first": 1,
                "second": 3
            }
        ])

class TestSolve(unittest.TestCase):
    @mock.patch("numpy.array", return_value=np.array(list("abcde")))
    def test_part1(self, mocked):
        self.assertEqual(solve("s1,x3/4,pe/b"), "baedc")
    