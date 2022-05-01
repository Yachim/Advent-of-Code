from copy import deepcopy

with open("input.txt", "r") as f:
    input = [tuple(map(int, i.split("-"))) for i in f.read().splitlines()]

def part1():
    inpt = deepcopy(input)
    ip = min(inpt, key=lambda x: x[1])
    inpt.remove(ip)
    ip = ip[1] + 1
    while any(s <= ip <= e for s, e in input):
        ip = min(inpt, key=lambda x: x[1])
        inpt.remove(ip)
        ip = ip[1] + 1
    return ip

def part2():
    inpt = deepcopy(input)
    allowed = 0
    while inpt:
        ip = min(inpt, key=lambda x: x[1])
        inpt.remove(ip)
        ip = ip[1] + 1
        if not any(s <= ip <= e for s, e in input):
            allowed += 1
    return allowed - 1

print(part1())
print(part2())