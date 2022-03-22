from collections import Counter
from functools import reduce
from itertools import combinations
from operator import mul

input = tuple(map(int, open("input.txt", "r").read().splitlines()))

def solve(parts=3):
    target_sum = int(sum(input)/parts)
    combs = (combinations(input, i) for i in range(len(input)))
    return find(parts, target_sum, combs)

def find(parts, target, combs, sub=tuple(), current_parts=1):
    if current_parts == parts:
        return True
    for i in combs:
        for j in i:
            weights_used = sub + j
            if sum(j) == target and len(weights_used) == len(set(weights_used)):
                if find(parts, target, combs, j, current_parts + 1):
                    return reduce(mul, j)

print(solve())
print(solve(4))