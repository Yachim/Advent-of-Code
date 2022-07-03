from subprocess import call
import unittest

from new_day import *

class TestInputProcessing(unittest.TestCase):
    def test_correct_format_1(self):
        self.assertEqual(process_input("2015;15"), ("AoC2015", "day15"))
    def test_correct_format_2(self):
        self.assertEqual(process_input("2015;1"), ("AoC2015", "day01"))

    def test_missing(self):
        with self.assertRaises(Exception) as ex:
            process_input("2015")
        self.assertTrue("Špatný formát vstupu" in str(ex.exception))

    def test_low_year(self):
        with self.assertRaises(Exception) as ex:
            process_input("2014;15")
        self.assertTrue("Moc nízký rok" in str(ex.exception))
    def test_high_year(self):
        with self.assertRaises(Exception) as ex:
            process_input("2089;15")
        self.assertTrue("Moc vysoký rok" in str(ex.exception))

    def test_low_day(self):
        with self.assertRaises(Exception) as ex:
            process_input("2015;0")
        self.assertTrue("Moc nízký den" in str(ex.exception))
    def test_high_day(self):
        with self.assertRaises(Exception) as ex:
            process_input("2015;30")
        self.assertTrue("Moc vysoký den" in str(ex.exception))

class FolderExists(unittest.TestCase):
    def test_year_folder_exists(self):
        self.assertTrue(folder_exists("AoC2015"))
    def test_year_folder_doesnt_exist(self):
        self.assertFalse(folder_exists("AoC2080"))

    def test_day_folder_exists(self):
        self.assertTrue(folder_exists("AoC2015/day15"))
    def test_day_folder_doesnt_exist(self):
        self.assertFalse(folder_exists("AoC2015/day0"))

class FolderEmpty(unittest.TestCase):
    def test_folder_empty(self):
        self.assertTrue(folder_empty("TestFolder"))
    def test_folder_not_empty(self):
        self.assertFalse(folder_empty("AoC2015/day01"))