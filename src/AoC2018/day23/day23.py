import re


RE = re.compile(r"^pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$", re.MULTILINE)

def process_input(raw_in: str):
    out = []
    for m in RE.finditer(raw_in):
        out.append(((int(m.group(1)), int(m.group(2)), int(m.group(3))), int(m.group(4))))

    return out


def part1(inp: list):
    strongest_pos, strongest_r = max(inp, key=lambda x: x[1])

    in_range = 0
    for pos, r in inp:
        x_dist = abs(pos[0] - strongest_pos[0])
        y_dist = abs(pos[1] - strongest_pos[1])
        z_dist = abs(pos[2] - strongest_pos[2])
        dist = x_dist + y_dist + z_dist

        if dist <= strongest_r: in_range += 1

    return in_range

def part2(inp):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")