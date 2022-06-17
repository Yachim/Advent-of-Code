from collections import Counter

input = list(zip(*[list(i) for i in open("input.txt", "r").read().splitlines()]))

def part1():
    out = ""
    for i in input:
        l = Counter(i).most_common(1)
        out += l[0][0]
    return out

def part2():
    out = ""
    for i in input:
        l = Counter(i).most_common()
        out += l[-1][0]
    return out

print(part1())
print(part2())