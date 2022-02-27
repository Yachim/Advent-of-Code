import re

input = open("input.txt", "r").read().splitlines()

RE1 = r"(children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes): (\d+)"
RE2 = r"Sue (\d+)"

aunt = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

def part1():
    for i in input:
        if (all(int(j.group(2)) == aunt[j.group(1)] for j in re.finditer(RE1, i))):
            return re.match(RE2, i).group(1)
        
def part2():
    for i in input:
        matches = list(re.finditer(RE1, i))
        if matches[0].group(1) in ["cats", "trees"]:
            found = int(matches[0].group(2)) > aunt[matches[0].group(1)]
        elif matches[0].group(1) in ["pomeranians", "goldfish"]:
            found = int(matches[0].group(2)) < aunt[matches[0].group(1)]
        else:
            found = int(matches[0].group(2)) == aunt[matches[0].group(1)]
        matches.pop(0)
        for j in re.finditer(RE1, i):
            if j.group(1) in ["cats", "trees"]:
                found = found and int(j.group(2)) > aunt[j.group(1)]
            elif j.group(1) in ["pomeranians", "goldfish"]:
                found = found and int(j.group(2)) < aunt[j.group(1)]
            else:
                found = found and int(j.group(2)) == aunt[j.group(1)]
        if found:
            return re.match(RE2, i).group(1)    

print(part1())
print(part2())