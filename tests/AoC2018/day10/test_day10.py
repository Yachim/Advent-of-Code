from concurrent.futures import process
import unittest
            
from src.AoC2018.day10.day10 import *

test_input = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input("""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>"""), [
    {
        "pos_x": 9, "pos_y": 1,
        "vel_x": 0, "vel_y": 2
    },
    {
        "pos_x": 7, "pos_y": 0,
        "vel_x": -1, "vel_y": 0
    },
    {
        "pos_x": 3, "pos_y": -2,
        "vel_x": -1, "vel_y": 1
    }
])

class TestGridRender(unittest.TestCase):
    def test1(self):
        grid = [
            {"pos_x": 0, "pos_y": 1},
            {"pos_x": 1, "pos_y": 1}
        ]

        self.assertEqual(render_grid(grid, 0, 1), """..
##""")
    def test2(self):
        grid = [
            {"pos_x": 0, "pos_y": 1},
            {"pos_x": 1, "pos_y": 0},
            {"pos_x": 2, "pos_y": 1}
        ]

        self.assertEqual(render_grid(grid, 0, 1), """.#.
#.#""")
        
class TestPart1(unittest.TestCase):
    def test(self):
        print(solve(process_input(test_input))) # HI
    def test_at_sec(self):
        print(part1_at_sec(process_input(test_input), 3)) # HI
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(process_input(test_input), True), 10656)