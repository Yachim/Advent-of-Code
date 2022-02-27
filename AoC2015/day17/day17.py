from itertools import permutations

input = list(map(int, open("input.txt", "r").read().splitlines()))

def part1(subset=[], remaining=input): # vraci none
    if sum(subset) > 150:
        return
    elif sum(subset) == 150:
        yield subset
    for i, j in enumerate(remaining):
        yield from part1(subset+[j], remaining[i+1:])
       
print(print(len(list(part1()))))
print(print(len(min(list(part1()), key=lambda x: len(x)))))