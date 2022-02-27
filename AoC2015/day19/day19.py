import re
from time import time

input = open("input.txt", "r").read().split("\n\n")

RE1 = "(\w+) => (\w+)"
RE2 = "([A-Z]{1}[a-z]{0,1})"

input[1] = tuple(re.findall(RE2, input[1]))
replacements = {i.group(1):[] for i in re.finditer(RE1, input[0])}
for i in re.finditer(RE1, input[0]):
    replacements[i.group(1)].append(tuple(re.findall(RE2, i.group(2))))
input[0] = replacements 

max_molecules = max(len(i) for j in list(input[0].values()) for i in j) # max molecules in one replacements

def part1():
    combs = set()
    for i, j in enumerate(input[1]):
        if j in input[0].keys():
            for k in input[0][j]:
                combs.add(input[1][:i] + k + input[1][i+1:])
    return len(combs)

calls = 0
def part2(m=input[1], steps=0):
    global calls
    calls += 1
    if m == "e":
        yield steps
    else:
        for i in input[0]:
            for j in input[0][i]:
                for k in range(0, len(m)-len(j)):
                    sub = m[k:k+len(j)]
                    if sub == j:
                        yield from part2(m[:k] + (i,) + m[k+len(j):], steps+1)
    return

print(part1())
t = time()
print(min(part2()))
print(calls, time() - t)