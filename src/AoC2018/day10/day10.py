from copy import deepcopy
import re


INPUT_RE = re.compile("position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>", re.MULTILINE)

def process_input(raw_in: str):
    out = []
    for i in INPUT_RE.finditer(raw_in):
        out.append({
            "pos_x": int(i.group(1)),
            "pos_y": int(i.group(2)),
            "vel_x": int(i.group(3)),
            "vel_y": int(i.group(4))
        })
    
    return out

def render_grid(grid: list, min_y: int, max_y: int) -> str:
    min_x = min(grid, key=lambda x: x["pos_x"])["pos_x"]
    max_x = max(grid, key=lambda x: x["pos_x"])["pos_x"]
    row_len = max_x - min_x + 1

    rows = []

    for i in range(min_y, max_y + 1):
        row = ["."] * row_len
        row_data = filter(lambda x: x["pos_y"] == i, grid)

        for j in row_data:
            index = j["pos_x"] - min_x
            row[index] = "#"

        rows.append("".join(row))
    
    return "\n".join(rows)        

def solve(inp: list, part2 = False):
    grid = deepcopy(inp)
    iteraction_cnt = 0

    while True:
        min_y = min(grid, key=lambda x: x["pos_y"])["pos_y"]
        max_y = max(grid, key=lambda x: x["pos_y"])["pos_y"]

        if max_y - min_y <10: 
            if part2: return iteraction_cnt
            return render_grid(grid, min_y, max_y)

        for i in grid:
            i["pos_x"] += i["vel_x"]
            i["pos_y"] += i["vel_y"]

        iteraction_cnt += 1

def part1_at_sec(inp: list, secs: int):
    grid = deepcopy(inp)

    for i in grid:
        i["pos_x"] += i["vel_x"] * secs
        i["pos_y"] += i["vel_y"] * secs
    
    min_y = min(grid, key=lambda x: x["pos_y"])["pos_y"]
    max_y = max(grid, key=lambda x: x["pos_y"])["pos_y"]

    spread = max_y - min_y
    print(f"spread: {spread}")
    if spread > 10: return
    return render_grid(grid, min_y, max_y)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: \n{part1_at_sec(inp, 10656)}\n\n") # xlzakbgz
    print(f"Part 1: \n{solve(inp)}\n\n")
    print(f"Part 1: \n{solve(inp, True)}\n\n")