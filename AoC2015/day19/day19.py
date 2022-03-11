from audioop import reverse
from pyexpat import model
import re
from collections import Counter

input = open("input.txt", "r").read().split("\n\n")

RE1 = "(\w+) => (\w+)"
RE2 = "([A-Z]{1}[a-z]{0,1})"

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

def part2(m=input[1], steps=0):
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

"""def part2():
    graph = {input[1]:set()}
    i = 0
    while set() in graph.values():
        key = list(graph.keys())[i]
        for j in reverse_replacements:
            for k in re.finditer(j, key):
                new_str = key[k.start():] + reverse_replacements[j] + key[:k.end()]
                if "e" in new_str and len(new_str) > 1:
                    continue
                graph[key].add(new_str)
                if new_str not in graph:
                    graph[new_str] = set()
        if graph[key] == set():
            graph.pop(key)
        else:
            i += 1
    print()
"""
def part2():
    graph = [[input[1]]]
    i = 0
    while True:
        graph.append([])
        mols = graph[i]
        for l in mols:
            for j in reverse_replacements:
                for k in re.finditer(j, l):
                    new_str = l[k.start():] + reverse_replacements[j] + l[:k.end()]
                    if new_str == "e":
                        return i + 1
                    if "e" in new_str and len(new_str) > 1:
                        continue
                    graph[i+1].append(new_str)
            i += 1

print(part1())
print(part2())