with open("input.txt", "r") as f:
    input = list(map(int, f.read().splitlines()))

def solve(part2 = False):
    i = 0
    steps = 0
    inpt = input.copy()
    while i < len(inpt) and i >= 0:
        offset = inpt[i]
        if offset >= 3 and part2:
            inpt[i] -= 1
        else:
            inpt[i] += 1
        i += offset
        steps += 1

    return steps


print(solve())
print(solve(True))