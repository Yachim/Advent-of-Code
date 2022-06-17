import re
from itertools import permutations

input = open("input.txt", "r").read().splitlines()

RE1 = r"^(\w+) would gain (\d+) happiness units by sitting next to (\w+).$" # how much would they gain
RE2 = r"^(\w+) would lose (\d+) happiness units by sitting next to (\w+).$" # how much would they lose

sitting_dict = {}
people = []
for i in input:
    match = re.match(RE1, i) if "gain" in i else re.match(RE2, i)
    h = int(match.group(2)) if "gain" in i else -int(match.group(2))
    sitting_dict[match.group(1)+":"+match.group(3)] = h
    people += [match.group(1), match.group(3)]
people = list(set(people))
combs = permutations(people)

def calculate_happiness(comb):
    s = 0
    if comb[-1] != "me" and comb[0] != "me":
        s += sitting_dict[comb[-1]+":"+comb[0]] # sum
        s += sitting_dict[comb[0]+":"+comb[-1]] 
    for i in range(1, len(comb)):
        if comb[i] != "me" and comb[i-1] != "me":
            s += sitting_dict[comb[i]+":"+comb[i-1]]
            s += sitting_dict[comb[i-1]+":"+comb[i]]
    return s

def part1():
    return calculate_happiness(max(combs, key=calculate_happiness))

def part2():
    combs = permutations(people + ["me"])
    return calculate_happiness(max(combs, key=calculate_happiness))

print(part1())
print(part2())