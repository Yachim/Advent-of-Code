from copy import deepcopy

input = open("input.txt", "r").read().splitlines()
for i, j in enumerate(input):
    input[i] = [int(k) for k in j.strip().split()]

def part1():
    inpt = deepcopy(input)
    valid = 0
    for i in inpt:
        i.sort()
        if int(i[0]) + int(i[1]) > int(i[2]):
            valid += 1
    return valid

def part2():
    valid = 0
    inpt = zip(*input)
    for i in inpt:
        for j in range(0, len(i)-2, 3):
            arr = sorted([i[j], i[j+1], i[j+2]])
            if int(arr[0]) + int(arr[1]) > int(arr[2]):
                valid += 1
    return valid

print(part1())
print(part2())