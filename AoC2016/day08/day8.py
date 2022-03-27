import numpy as np
import re

input = open("input.txt", "r").read().splitlines()

RE1 = r"(?:rect) (?:(\d+)x(\d+))"
RE2 = r"(?:rotate (?:row|column)) (x|y)=(\d+) by (\d+)"

def solve(h, w, part2=False):
    grid = np.zeros((h, w))
    for i in input:
        if re.match(RE1, i):
            m = re.match(RE1, i)
            w = int(m.group(1))
            h = int(m.group(2))
            grid[:h, :w] = np.ones((h, w))
        elif re.match(RE2, i):
            m = re.match(RE2, i)
            axis = m.group(1)
            pos = int(m.group(2))
            shift = int(m.group(3))
            
            if axis == "x":
                grid[:,pos] = np.roll(grid[:,pos], shift)
            elif axis == "y":
                grid[pos] = np.roll(grid[pos], shift)
        
    if part2:
        res = ""
        for i in grid:
            i = str(i)
            i = re.sub(r"\n|\[|\]|\.| ", "", i)
            i = i.replace("1", "#")
            i = i.replace("0", ".")
            res += i + "\n"
        return res[:-1]
    else:
        return int(sum(sum(grid)))

print(solve(6, 50))
print(solve(6, 50, True))