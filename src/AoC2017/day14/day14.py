import sys

if __name__ == "__main__":
    sys.path.append("../../..")
from src.AoC2017.day10.day10 import part2 as knot_h


def get_binary(inp: str):
    return "".join([bin(int(i, 16))[2:].zfill(4) for i in inp])

def create_grid(inp: str):
    grid = []
    for i in range(128):
        knot = knot_h(256, f"{inp}-{i}") 
        b = get_binary(knot)
        grid.append([bool(int(i)) for i in b])

    return grid

def update_cell(grid: list, line_index: int, cell_index: int):
    try:
        if not grid[line_index][cell_index]: return
    except:
        print()
    grid[line_index][cell_index] = False
    

    if line_index > 0: update_cell(grid, line_index - 1, cell_index)
    if line_index < len(grid) - 1: update_cell(grid, line_index + 1, cell_index)
    if cell_index > 0: update_cell(grid, line_index, cell_index - 1)
    if cell_index < len(grid[line_index]) - 1: update_cell(grid, line_index, cell_index + 1)


def part1(inp: str):
    grid = create_grid(inp)
    return sum(sum(i) for i in grid)

def part2(inp: str):
    grid = create_grid(inp).copy()
    total = 0
    for line_index, line in enumerate(grid):
        for cell_index, cell in enumerate(line):
            if not cell: continue
            update_cell(grid, line_index, cell_index)
            total += 1

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.read()

    print(part1(inp))
    print(part2(inp))
    