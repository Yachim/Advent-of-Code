with open("input.txt", "r") as f:
    input = [[int(j) for j in i.split()] for i in f.read().splitlines()]

def part1():
    return sum([max(i) - min(i) for i in input])

def part2():
    s = 0
    for i in input:
        for j, l in enumerate(i):
            for k in i[:j] + i[j+1:]:
                if l % k == 0:
                    s += l / k
    return int(s)

print(part1())
print(part2())