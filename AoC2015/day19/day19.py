from audioop import reverse
from pyexpat import model
import re
from collections import Counter

input = open("input.txt", "r").read().split("\n\n")

RE1 = r"(\w+) => (\w+)"
RE2 = r"([A-Z]{1}[a-z]{0,1})"

replacements = {i.group(1):[] for i in re.finditer(RE1, input[0])}
for i in re.finditer(RE1, input[0]):
    replacements[i.group(1)].append(i.group(2))
input[0] = replacements
reverse_replacements = {j:i for i in input[0] for j in input[0][i]}

def part1():
    combs = set()
    inpt = tuple(re.findall(RE2, input[1]))
    for i, j in enumerate(inpt):
        if j in input[0]:
            for k in input[0][j]:
                combs.add((inpt[:i]) + tuple(re.findall(RE2, k)) + (inpt[i+1:]))
    return len(combs)

# u/askalski's solution (https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/?utm_source=share&utm_medium=web2x&context=3)
def part2r():
    total = len(re.findall(RE2, input[1]))
    return total - input[1].count("Rn") - input[1].count("Ar") - 2*input[1].count("Y") - 1

def part2():
    i = 0
    mol = input[1]
    while mol != "e":
        i += 1
        mols = set()
        for j in reverse_replacements:
            for k in re.finditer(j, mol):
                mols.add(mol[:k.start()] + reverse_replacements[j] + mol[k.end():])
        mol = min(mols, key=lambda x: len(re.findall(RE2, x)))
    return i

print(part1())
print(part2())
print(part2r())