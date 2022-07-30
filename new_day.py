from typing import Tuple
from os.path import isdir
from os import mkdir, listdir
from venv import create

def process_input(inp: str) -> Tuple[str, str]:
    inp = [int(i.strip()) for i in inp.split(";")]
    if len(inp) != 2: raise Exception("Špatný formát vstupu")
    [year, day] = inp
    if year < 2015: raise Exception("Moc nízký rok")
    if year > 2021: raise Exception("Moc vysoký rok")
    if day < 1: raise Exception("Moc nízký den")
    if day > 25: raise Exception("Moc vysoký den")

    return (f"AoC{year}", f"day{str(day).zfill(2)}")

def folder_exists(folder_name: str) -> bool:
    return isdir(f"src/{folder_name}/")

def folder_empty(folder_name: str) -> bool:
    dir = listdir(f"src/{folder_name}")
    return len(dir) == 0 or (len(dir) == 1 and "__init__.py" in dir)

def create_folder(path: str):
    mkdir(path)
    f = open(f"{path}/__init__.py", "x")
    f.close()

def create_files(path: str, day: str, name_pref=""):
    f = open(f"{path}/__init__.py", "x")
    f = open(f"{path}/{name_pref}{day}.py", "x")
    f = open(f"{path}/{name_pref}input.txt", "x")
    f.close()

if __name__ == "__main__":
    [year, day] = process_input(input("Formát: [číslo roku];[číslo dne], např. 2019;1\n"))

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
            f.write(f"import unittest\n\nfrom src.{year}.{day}.{day} import *")

        with open(f"src/{year}/{day}/{day}.py", "w") as f:
            f.write('''

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")''')
