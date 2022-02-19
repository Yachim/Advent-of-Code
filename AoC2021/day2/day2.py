test = False

file_name = "input.txt" if not test else "testInput.txt"
input = open(file_name, "r").read().splitlines()

def part1():
    horizontal = 0
    depth = 0
    for i in input:
        i = i.split(" ")
        if i[0] == "forward":
            horizontal += int(i[1])
        elif i[0] == "down":
            depth += int(i[1])
        elif i[0] == "up":
            depth -= int(i[1])

    return horizontal*depth

def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for i in input:
        i = i.split(" ")
        if i[0] == "forward":
            horizontal += int(i[1])
            depth += aim*int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])

    return horizontal*depth

print(part1())
print(part2())