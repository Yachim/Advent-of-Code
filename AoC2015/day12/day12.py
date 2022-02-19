import re
import json
from numpy import isin

from pkg_resources import yield_lines

input = open("input.txt", "r").read()

RE = r"-{0,1}\d+"

def part1():
    return sum([int(i) for i in re.findall(RE, input)])

def part2(inpt=json.loads(input)): #s...sum
    s = 0
    if (isinstance(inpt, dict) and ("red" in inpt.keys() or "red" in inpt.values())) or isinstance(inpt, str):
        s += 0
    elif isinstance(inpt, int):
        s +=  inpt
    else:
        for i in inpt:
            if isinstance(inpt, dict):
                s += part2(inpt[i])
            else:
                s += part2(i)
    return s


print(part1())
print(part2())