input = open("input.txt", "r").read()

def part1():
    up = input.count("(")
    down = input.count(")")
    return up-down

def part2():
    floor = 0
    for i in range(len(input)):
        floor += {"(": 1, ")": -1}[input[i]]
        if floor < 0:
            return i+1



print(part1())
print(part2())