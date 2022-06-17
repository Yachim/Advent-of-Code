from collections import Counter
from functools import reduce
from operator import mul
import re

input = open("input.txt", "r").read()

RE = r"^Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)\.$"

discs = []
for i, j in enumerate(re.finditer(RE, input, re.M), 1):
    pos = int(j.group(1)) # number of positions
    pos_at = int(j.group(2)) + i # position at time equal to disk's number - position at the time it reaches the disk
    if pos_at >= pos:
        pos_at = pos_at % pos
    discs.append((pos, pos_at))

def part1():
    ts = [[] for i in range(len(discs))]
    for i, j in enumerate(discs):
        t = j[0] - j[1] # time it takes to reach position 0

        for k in range(2, t + 1):
            prime = True
            for l in ts[i]:
                if k % l == 0:
                    prime = False
                    break
            if t % k != 0 or not prime:
                continue
            
            while t % k == 0:
                ts[i].append(k)
                t /= k

    all_primes = set(ts[0])
    for i in ts[1:]:
        all_primes = all_primes.union(i)
    
    time = 1
    for i in all_primes:
        time *= i * max(j.count(i) for j in ts)
    
    return time

print(part1())