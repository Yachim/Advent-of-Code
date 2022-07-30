def process_input(raw_in):
    return list(map(int, raw_in.splitlines()))

def part1(inp):
    return sum(inp)

def part2(inp):
    current_val = 0
    reached_vals = {0,}
    while True:
        for i in inp:
            current_val += i
            if current_val in reached_vals:
                return current_val

            reached_vals.add(current_val)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")