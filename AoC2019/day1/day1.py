input = [int(i) for i in open("input.txt", "r").read().splitlines()]

def part1():
    values = input.copy()
    return sum(int(item/3)-2 for item in values)

def part2():
    values = input.copy()
    total = 0
    for i in values:
        while int(i/3)-2 > 0:
            i = int(i/3)-2
            total += i
    return total

print(part1())
print(part2())