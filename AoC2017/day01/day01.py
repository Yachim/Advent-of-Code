with open("input.txt", "r") as f:
    input = f.read()

def solve(part2=False):
    l = len(input)
    indexes = range(l)
    if part2:
        valid_indexes = filter(lambda x: input[x] == input[x-int(l/2)], indexes)
    else:
        valid_indexes = filter(lambda x: input[x] == input[x-1], indexes)
    return sum(map(lambda x: int(input[x]), valid_indexes))

print(solve())
print(solve(True))