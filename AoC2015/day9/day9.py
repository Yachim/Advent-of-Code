from itertools import permutations
from math import perm

distances = {}
input = open("input.txt", "r").read().splitlines()
for i in input:
    i = i.split(" ")
    distances[i[0]+":"+i[2]] = int(i[4])
    distances[i[2]+":"+i[0]] = int(i[4])

destinations = []
for i in distances.keys():
    destinations += i.split(":")
destinations = list(set(destinations))
combinations = list(permutations(destinations))

def part1():
    lowest = min(combinations, key=lambda x: sum(distances[x[i]+":"+x[i+1]] for i in range(len(x)-1))) # array with lowest distance
    return sum(distances[lowest[i]+":"+lowest[i+1]] for i in range(len(lowest)-1))

def part2():
    highest = max(combinations, key=lambda x: sum(distances[x[i]+":"+x[i+1]] for i in range(len(x)-1))) # array with highest distance
    return sum(distances[highest[i]+":"+highest[i+1]] for i in range(len(highest)-1))

print(part1())
print(part2())