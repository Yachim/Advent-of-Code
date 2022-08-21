import unittest
            
from src.AoC2018.day04.day04 import *


class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input(
"""[1518-11-01 00:25] wakes up
[1518-11-01 00:05] falls asleep
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 00:00] Guard #10 begins shift"""
        ), {10: ["1518-11-01 00:05...1518-11-01 00:25", "1518-11-01 00:30...1518-11-01 00:55"]})
        
class TestGetMinutes(unittest.TestCase):
    def test(self):
        self.assertEqual(get_minutes("1518-11-01 00:05...1518-11-01 00:25"), 20)

class TestGetMinutesAsleep(unittest.TestCase):
    def test(self):
        self.assertEqual(get_minutes_asleep("1518-11-01 00:05...1518-11-01 00:10"), [5, 6, 7, 8, 9])

class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(process_input("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""")), 240)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(process_input("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""), True), 4455)