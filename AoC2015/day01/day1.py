input = open("input.txt", "r").read()

instructions = {"(": 1, ")": -1}

def part1():
    up = input.count("(")
    down = input.count(")")
    return up-down

def part2():
    floor = 0
    for i, j in enumerate(input):
        floor += instructions[j]
        if floor < 0:
            return i+1



print(part1())
print(part2())