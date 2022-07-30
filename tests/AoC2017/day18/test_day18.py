import unittest

from src.AoC2017.day18.day18 import *

class TestInputProcessing(unittest.TestCase):
    def test(self):
        ins, regs = process_input("""set a 1
add b 2
set b c""")
        self.assertEqual(ins, [
            {
                "in": "set",
                "reg": "a",
                "val": 1
            },
            {
                "in": "add",
                "reg": "b",
                "val": 2
            },
            {
                "in": "set",
                "reg": "b", 
                "val": "c"
            }
        ])
        self.assertEqual(regs, {"a", "b", "c"})

class TestPart1(unittest.TestCase):
    def test(self):
        ins, regs = process_input("""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""")
        self.assertEqual(part1(ins, regs), 4)

class TestPart2(unittest.TestCase):
    def test(self):
        ins, regs = process_input("""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""")
        self.assertEqual(part2(ins, regs), 3)