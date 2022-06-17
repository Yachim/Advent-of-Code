from itertools import combinations, permutations
import re

RE = re.compile(r"^[a-z\/]+-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$", re.MULTILINE) 
# group 1: x
# group 2: y
# group 3: size
# group 4: used
# group 5: avail
# group 6: percentage

input = {}
with open("input.txt", "r") as f:
    for i in RE.finditer(f.read()):
        input[(int(i.group(1)), int(i.group(2)))] = (int(i.group(3)), int(i.group(4)), int(i.group(5)), int(i.group(6))) # (size, used, avail, percentage)

def part1():
    combs = combinations(input, 2)
    valid = 0
    for i in combs:
        a = input[i[0]]
        b = input[i[1]]
        if a[1] != 0 and a[1] <= b[2]:
            valid += 1
        if b[1] != 0 and b[1] <= a[2]:
            valid += 1
    return valid

def part2():
    empty = next(filter(lambda x: input[x][1] == 0, input))
    print()

        
print(part1())
print(part2())