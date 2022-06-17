from json import loads
import re

RE_NEGATION = re.compile(r"!.")
RE_GARBAGE = re.compile(r"<.*?>")
RE_COMMAS = re.compile(r",+(?=})|(?<={),+")

RE_GARBAGE_2 = re.compile(r"<.*?>")

with open("input.txt", "r") as f:
    input = f.read()

def get_group_score(sub, depth=1):
    if len(sub) == 0:
        return depth

    s = depth
    for i in sub:
        s += get_group_score(i, depth+1)
    return s

def part1():
    inpt = RE_NEGATION.sub("", input)
    inpt = RE_GARBAGE.sub("", inpt)
    inpt = RE_COMMAS.sub("", inpt)
    inpt = inpt.replace("{", "[")
    inpt = inpt.replace("}", "]")

    inpt = loads(inpt)
    return get_group_score(inpt)

def part2(): 
    inpt = RE_NEGATION.sub("", input)

    s = 0
    for i in RE_GARBAGE_2.finditer(inpt):
        s += len(i.group(0)) - 2

    return s

print(part1())
print(part2())