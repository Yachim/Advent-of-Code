from itertools import permutations


with open("input.txt", "r") as f:
    grid = f.read().splitlines()
    input = []
    pois = {} # points of interest
    for i, j in enumerate(grid):
        for k, l in enumerate(j):
            if l == ".":
                input.append((k, i))
            elif l.isnumeric():
                pois[int(l)] = (k, i)
                input.append((k, i))

def part1():
    perms = permutations(pois.keys(), len(pois.keys()))
    x = 0
    for i in perms:
        x += 1
    print()

print(part1())