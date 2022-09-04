from typing import Tuple
from os.path import isdir
from os import mkdir, listdir
from venv import create

def process_input(inp: str) -> Tuple[str, str]:
    inp = [int(i.strip()) for i in inp.split(";")]
    if len(inp) != 2: raise Exception("Bad input format")
    [year, day] = inp
    if year < 2015: raise Exception("Year too low")
    if year > 2021: raise Exception("Year too high")
    if day < 1: raise Exception("Day too low")
    if day > 25: raise Exception("Day too high")

    return (f"AoC{year}", f"day{str(day).zfill(2)}")

def folder_exists(folder_name: str) -> bool:
    return isdir(f"src/{folder_name}/")

def folder_empty(folder_name: str) -> bool:
    dir = listdir(f"src/{folder_name}")
    return len(dir) == 0 or (len(dir) == 1 and "__init__.py" in dir)

def create_folder(path: str):
    mkdir(path)

def create_files(path: str, day: str, name_pref=""):
    f = open(f"{path}/{name_pref}{day}.py", "x")
    f.close()
    # no test_input
    if name_pref == "":
        f = open(f"{path}/input.txt", "x")
        f.close()
    f = open(f"{path}/__init__.py", "x")
    f.close()

if __name__ == "__main__":
    [year, day] = process_input(input("Format: [year];[day], ie. 2019;1\n"))

    if not folder_exists(year):
        create_folder(f"src/{year}")
        create_folder(f"tests/{year}")

    if not folder_exists(f"{year}/{day}"):
        create_folder(f"src/{year}/{day}")
        create_folder(f"tests/{year}/{day}")

    if folder_empty(f"{year}/{day}"):
        create_files(f"src/{year}/{day}", day)
        create_files(f"tests/{year}/{day}", day, "test_")

        with open(f"tests/{year}/{day}/test_{day}.py", "w") as f:
            f.write(f"""import unittest
            
from src.{year}.{day}.{day} import *


class TestInputProcessing(unittest.TestCase):
    def test(self):
        self.assertEqual(process_input(), None)
        
class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1(), None)
        
class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2(), None)""")

        with open(f"src/{year}/{day}/{day}.py", "w") as f:
            f.write('''def process_input(raw_in: str):
    pass

def part1(inp):
    pass

def part2(inp):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")''')
