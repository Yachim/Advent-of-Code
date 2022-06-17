from collections import Counter


with open("input.txt", "r") as f:
    input = [i.split(" ") for i in f.read().splitlines()]

def part1():
    valid = 0
    for i in input:
        cnt = Counter(i).most_common()[0][1]
        if cnt == 1:
            valid += 1
    return valid

def part2():
    valid = 0
    for i in input:
        arr = ["".join(sorted(j)) for j in i]
        cnt = Counter(arr).most_common()[0][1]
        if cnt == 1:
            valid += 1
    return valid

print(part1())
print(part2())