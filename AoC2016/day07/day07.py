import re

input = open("input.txt", "r").read().splitlines()

RE_ABBA = r"(\w)((?!\1)\w)\2\1"
RE_ABA = r"(?=(\w)((?!\1)\w)\1)" # lookahead so it is zero width and can overlap

def part1():
    s = 0
    for i in input:
        ip = re.split("\[|\]", i)
        supernet = ",".join(ip[::2])
        hypernet = ",".join(ip[1::2])
        if re.search(RE_ABBA, supernet) and not re.search(RE_ABBA, hypernet):
            s += 1
    return s

def part2():
    s = 0
    for i in input:
        ip = re.split("\[|\]", i)
        supernet = ",".join(ip[::2])
        hypernet = ",".join(ip[1::2])

        for i in re.finditer(RE_ABA, supernet):
            a = i.group(1)
            b = i.group(2)
            if b + a + b in hypernet:
                s += 1
                break
    return s

print(part1())
print(part2())