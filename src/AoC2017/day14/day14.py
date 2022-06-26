import sys
from venv import create

if __name__ == "__main__":
    sys.path.append("../../..")
from src.AoC2017.day10.day10 import part2

def get_binary(inp: str):
    return bin(int(inp, 16))[2:].zfill(4)

def create_grid(inp: str):
    grid = []
    for i in range(128):
        knot = part2(256, f"{inp}-{i}") 
        b = get_binary(knot)
        grid.append(bool(int(i)) for i in b)

    return grid

def part1(inp: str):
    grid = create_grid(inp)
    return sum(sum(i) for i in grid)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.read()

    print(part1(inp))
    